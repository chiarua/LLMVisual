from . import utils
from .TextGen import TextGenerator


class Initialize:

    def __init__(self, textgen=TextGenerator()):
        self.instr = None
        self.persona = None
        self.field_descr = None
        self.questions = None
        self.dataset_descr = None
        self.dataset_name = None
        self.chart_set = dict()
        self.textgen = textgen

    def initialize(self, data) -> None:
        preview: dict = self.textgen.dataset_preview(data)['preview']
        self.dataset_name: str = preview['name']
        self.dataset_descr: str = preview['dataset_description']
        self.field_descr: dict = preview['field_description']
        self.questions: list = preview['questions']
        self.persona = utils.load_prompts(query="VEGALITE_PROMPT")  # 生成图表提示词

    def generate(self, question: str):
        """
        for generating charts.
        :param question: a question as string
        :return: charts with explains
        """
        self.instr = 'name: ' + self.dataset_name + '; dataset_description: ' + self.dataset_descr \
                      + '; field_description: ' + str(self.field_descr) + '; the question: '
        persona = self.persona
        instruction = self.instr + question
        message = self.textgen.generate(persona, instruction)
        return message['visualization_list']

    def get_persona(self) -> str:
        return self.persona

    def get_questions(self) -> list:
        return self.questions

    def get_dataset_prev(self) -> str:
        return self.dataset_descr

    def get_field_prev(self) -> str:
        return self.field_descr