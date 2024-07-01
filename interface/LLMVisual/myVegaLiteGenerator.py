from . import Initial

import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"


class VegaLiteGenerator:
    def __init__(self):
        self.explanation = []
        self.codes = []
        self.initialize = Initial.Initialize()
        self.initialize.initialize("D:\\UPC DL\\ChartSeer\\interface\\staticdata\\cars.json")
        self.persona = self.initialize.get_persona()
        self.visualization_list = []

    def generate(self, question: str):
        persona = self.persona
        # Todo: add sample charts? if we should?
        instruction = 'name: ' + self.initialize.dataset_name + '; dataset_description: ' + self.initialize.dataset_descr \
                      + '; field_description: ' + str(self.initialize.field_descr) + '; the question: ' + question
        message = self.initialize.textgen.generate(persona, instruction)
        self.visualization_list = message['visualization_list']
        self.codes = [element['vega-lite_code'] for element in message if 'vega-lite_code' in element['message']]
        self.explanation = [element['explanation'] for element in message if 'vega-lite_code' in element['message']]

    def get_codes(self):
        return self.codes

    def get_explanation(self):
        return self.explanation