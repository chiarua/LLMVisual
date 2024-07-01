import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

json_path = os.path.join(dir_path, 'model_prompts.json')
spec_path = os.path.join(dir_path, 'rules-cfg.txt')


def load_prompts(path=json_path, query: str = ''):
    with open(path, 'r', encoding='utf-8') as f:
        prompts = json.load(f)
    if not query:
        return prompts
    return prompts[query]


def parse_specs():
    '''
    'color': [['aggregate', 'field', 'type'], ['bin', 'field', 'type'], ...
    '''
    with open(spec_path, 'r') as f:
        specs = f.read()

    spec_dict = {}
    lines = specs.strip().split('\n')
    for line in lines:
        key, value = line.split(' -> ')
        values = value.split('+')
        nv = []
        for v in values:
            t = v.replace('"', '')
            t = t.replace(' ', '')
            nv.append(t)
        values = set(nv)
        if key not in spec_dict:
            spec_dict[key] = [values]
        else:
            spec_dict[key].append(values)
    return spec_dict


def fix_vegalite_spec_recur(json_spec, spec_dict):
    new_json_spec = {}
    for key in json_spec:
        value = json_spec[key]
        if key == "bin":
            new_json_spec[key] = value
        if isinstance(value, dict):
            if key not in spec_dict:
                new_json_spec[key] = fix_vegalite_spec_recur(value, spec_dict)
                continue
            tmp_spec = fix_vegalite_spec_recur(value, spec_dict)
            lst = set(list(tmp_spec.keys()))
            if lst not in spec_dict[key]:
                print(f"键 '{key}' 的值 '{lst}' 不在规范中")
            else:
                # print(f"键 '{key}' 的值 '{lst}' 在规范中")
                # new_json_spec[key] = fix_vegalite_spec_recur(value, spec_dict)
                new_json_spec[key] = tmp_spec
        elif isinstance(value, str):
            if key not in spec_dict:
                new_json_spec[key] = value
                continue
            if {value} not in spec_dict[key]:
                print(f"键 '{key}' 的值 '{value}' 不在规范中")
            else:
                new_json_spec[key] = value
    return new_json_spec


def check_root(spec):
    return set(spec.keys()) == {"encoding", "mark"}


def fix_charts(charts):
    fixed_charts = []
    the_spec = parse_specs()
    for chart in charts:
        chart['vega-lite_code'] = fix_vegalite_spec_recur(chart['vega-lite_code'], the_spec)
        fixed_charts.append(chart)
    del_lst = []
    for i, chart in enumerate(fixed_charts):
        if check_root(chart['vega-lite_code']):
            continue
        del_lst.append(i)
    print(del_lst)
    del_lst.reverse()
    for i in del_lst:
        charts.pop(i)
        fixed_charts.pop(i)
    dic = {"charts": charts, "charts_for_encode": fixed_charts}
    return dic


#print(parse_specs())
# specs = parse_specs()
# jstr = '''
# [
#         {
#             "explanation": "This scatter plot visualization shows the correlation between vehicle weight and horsepower, with each dot representing a vehicle. Different colors can be used to represent the production year.",
#             "question": "What are the trends in vehicle weight and horsepower over the years?",
#             "vega-lite_code": {
#                 "encoding": {
#                     "color": {
#                         "field": "Year",
#                         "timeUnit": "year",
#                         "type": "temporal"
#                     },
#                     "x": {
#                         "field": "Weight_in_lbs",
#                         "timeUnit": "year",
#                         "type": "quantitative"
#                     },
#                     "y": {
#                         "field": "Horsepower",
#                         "type": "quantitative"
#                     }
#                 },
#                 "mark": "point"
#             }
#         }, {
#             "explanation": "This visualization compares the trends of vehicle weight and horsepower over the years. A dual-axis chart allows for comparing both metrics in parallel, with production year on the x-axis.",
#             "question": "What are the trends in vehicle weight and horsepower over the years?",
#             "vega-lite_code": {
#                 "mark": "line"
#             }
#         }
#         ]
#     '''
# json_str = json.loads(jstr)

#check_vegalite_spec(json_str, specs)

# print(fix_vegalite_spec_recur(json_str, specs))
# print(check_root(json_str))
# print(fix_charts(json_str))