import json
import re
from multiprocessing import Pool
from typing import Dict, List

import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, jsonify, request
from flask_cors import CORS
from scipy.optimize import minimize
from scipy.spatial import procrustes
from sklearn.decomposition import PCA
from sklearn.manifold import MDS

from LLMVisual import VegaLiteGenerator
from gvaemodel.vis_vae import VisVAE
from LLMVisual.MainProcessor import FileUploadProcessor
from LLMVisual import utils

port = 5000
rulesfile = './gvaemodel/rules-cfg.txt'
modelsave = './gvaemodel/vae_H256_D256_C444_333_L20_B200.hdf5'
# rulesfile = './gvaemodel/rules-cfg2.txt'
# modelsave = './gvaemodel/vae_H256_D256_C888_333_L20_B200.hdf5'
# rulesfile = './gvaemodel/rules-cfg4.txt'
# modelsave = './gvaemodel/vae_H256_D256_C888_333_L20_B200.hdf5'


m = re.search(r'_L(\d+)_', modelsave)

# MAX_LEN = 20   #潜在空间的维度20
MAX_LEN = 20
LATENT = int(m.group(1))
# rules = []
# with open(rulesfile, 'r') as inputs:
#     for line in inputs:
#         line = line.strip()
#         rules.append(line)

# visvae = VisVAE(modelsave, rules, MAX_LEN, LATENT)
# graph = tf.get_default_graph()

# pca = PCA(n_components=2)

visvae = None
graph = None
sess = None
pca = None

app = Flask(__name__)
CORS(app)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    :return: json{"questions": list, "explanations": list}
    """
    file = request.files['file']
    if file.filename.endswith('.csv'):
        # 处理CSV文件
        df = pd.read_csv(file)
        data = csv_to_json(df)
    elif file.filename.endswith('.json'):
        # 处理JSON文件
        data = json.load(file)
    else:
        return "Unsupported file format", 400
    sample = data.get('attributes', [])
    sample_data = data.get('data', [])[:5]
    print(sample)
    processor.uploaded(str(sample))
    processor.get_sample(sample_data)
    return jsonify(processor.get_questions())
    # tmp = ['Which cars have the best fuel efficiency measured in Miles_per_Gallon?',
    #        'How does weight influence the acceleration of the automobiles?']
    #
    # return jsonify(tmp)


@app.route('/uploadjson', methods=['POST'])
def upload_json():
    """
    :return: json{"questions": list, "explanations": list}
    """
    data = request.get_json()
    sample = data.get('attributes', [])
    sample_data = data.get('data', [])[:5]
    processor.uploaded(str(sample))
    processor.get_sample(sample_data)
    return jsonify(processor.get_questions())


def csv_to_json(df):
    sample = df.to_dict(orient='records')
    attributes = []
    for column in df.columns:
        dtype = df[column].dtype
        if dtype == 'object':
            attributes.append([column, "str", ""])
        else:
            attributes.append([column, "num", ""])
    return {"charts": [], "attributes": attributes, "data": sample}


@app.route('/csvtojson', methods=['POST'])
def csvtojson():
    file = request.files['file']
    df = pd.read_csv(file)
    return jsonify(csv_to_json(df))


@app.route('/updatequiz', methods=['POST'])
def update_question():
    """
    :return: json{"chart": list, "charts_for_encode": list}
    """
    q = request.get_json()
    str_list = []
    if isinstance(q, list):
        # 将列表中的所有元素转换为字符串
        str_list = [str(item) for item in q]
    processor.update_questions(str_list)
    processor.generate_charts_ini()
    charts = processor.charts
    # print("these r charts")
    # print(charts)

    # 以下是sudo-output
    # json_data = json.dumps(charts)
    # # 将JSON数据写入文件
    # with open("tmpinput.json", "w") as file:
    #     file.write(json_data)
    # with open('tmpinput.json', 'r') as file:
    #     charts: List[dict] = json.load(file)

    dic = utils.fix_charts(charts)
    print(dic)
    return jsonify(dic), 200


@app.route('/addquiz', methods=['POST'])
def add_question():
    q = request.get_json()
    if isinstance(q, str):
        q = str(q)
    processor.add_question(q)
    return processor.generate_quiz_description(q)



@app.route('/modify', methods=['POST'])
def modify_chart():
    """
    :return: new chart-explanation which needs to replace the old one
    """
    # how to catch the request?
    req: dict = request.get_json()
    print(req)
    user_input = req.get("user_input")
    target_chart = req.get("target_chart")
    new_chart = processor.modify_charts(target_chart, user_input)
    return jsonify(new_chart), 200


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/encode', methods=['POST'])
def encode():
    specs = request.get_json()
    try:
        with graph.as_default():
            tf.keras.backend.set_session(sess)
            z = visvae.encode(specs)
    except Exception as e:
        raise InvalidUsage(e.message)
    return jsonify(z.tolist())


@app.route('/decode', methods=['POST'])
def decode():
    z = np.array(request.get_json())
    try:
        with graph.as_default():
            tf.keras.backend.set_session(sess)
            specs = visvae.decode(z)
    except Exception as e:
        raise InvalidUsage(e.message)
    return jsonify(specs)


@app.route('/decode_llm', methods=['POST'])
def decode_llm():
    req = request.get_json()
    print(req)
    chart = req["data"][0]
    idea = req["clientidea"]
    if idea != '':
        desc = processor.generate_chart_description_with_instr(str(chart), idea)
    else:
        desc = processor.generate_chart_description(str(chart))
    # res: Dict[str, list] = {"codes": [chart], "explanations": [desc]}
    print(desc)
    return jsonify(desc)


@app.route('/orientate', methods=['POST'])
def orientate():
    locations = request.get_json()
    mt1, mt2, disparity = procrustes(locations[0], locations[1])
    return jsonify(mt2.tolist())


@app.route('/pca', methods=['POST'])
def pcaproject():
    global pca
    pca = PCA(n_components=2)
    x = np.array(request.get_json())
    y = pca.fit_transform(x)
    return jsonify(y.tolist())


@app.route('/invpca', methods=['POST'])
def invpcaproject():
    global pca
    y = np.array(request.get_json())
    x = pca.inverse_transform(y)
    return jsonify(x.tolist())


@app.route('/mds', methods=['POST'])
def mdsproject():
    distm = np.array(request.get_json())
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=13, max_iter=3000, eps=1e-9)
    y = mds.fit(distm).embedding_
    # res = smacof(distm, n_components=2, random_state=13, max_iter=3000, eps=1e-9)
    # y = res[0]    
    return jsonify(y.tolist())


@app.route('/invmds', methods=['POST'])
def invmdsproject():
    inputdata = request.get_json()
    ps = np.array(inputdata['points'])
    dsall = np.array(inputdata['distances'])

    # res = myminimize((ps, dsall[0]))
    pool = Pool(8)
    res = pool.map(myminimize, [(ps, ds) for ds in dsall])
    res = [r.tolist() for r in res]
    pool.close()
    pool.join()
    return jsonify(res)


def myminimize(args):
    ps, ds = args
    x0 = np.random.random_sample(ps[0].shape)
    res = minimize(objfun, x0, args=(ps, ds), tol=1e-9, options={'maxiter': 3000})
    return res.x


def objfun(x, ps, ds):
    d = np.tile(x, (ps.shape[0], 1)) - ps
    d = np.sum(np.square(d), axis=1)
    diff = np.sqrt(d) - ds
    return np.sum(np.square(diff))

    # try:
    #     with graph.as_default():
    #         tf.keras.backend.set_session(sess)
    #         specs = visvae.decode(z)
    # except Exception as e:
    #     raise InvalidUsage(e.message)
    return jsonify(codes)


if __name__ == '__main__':
    rules = []
    with open(rulesfile, 'r') as inputs:  # 读cfg文件
        for line in inputs:
            line = line.strip()  # 删除头尾的空格
            rules.append(line)

    # sess一致方法
    sess = tf.Session()  # 创建一个新的TensorFlow会话
    tf.keras.backend.set_session(sess)

    visvae = VisVAE(modelsave, rules, MAX_LEN, LATENT)
    # 注意 modelsave = './gvaemodel/vae_H256_D256_C444_333_L20_B200.hdf5'
    # MAX_LEN = 20
    # LATENT = int(m.group(1))

    processor = FileUploadProcessor()

    graph = tf.get_default_graph()  # 返回当前线程的默认图形

    pca = PCA(n_components=2)  # 主成分分析

    app.run(host="127.0.0.1", port=port, debug=False)  # 在本地开发服务器上运行应用进程
