from typing import List

from .Initial import Initialize
from . import utils
from . import TextGen


class FileUploadProcessor:
    def __init__(self):
        self.quiz_desc_persona = None
        self.chart_desc_with_instr_persona = None
        self.chart_desc_persona = None
        self.field_preview: dict = None
        self.dataset_preview = None
        self.questions = None
        self.charts = []  # contains 'vega-lite_code', 'explanation', 'question'
        self.modify_persona = None
        self.question_expls = dict()
        self.ini = Initialize()
        self.sample = None

    def uploaded(self, dataset: str):
        self.ini.initialize(dataset)
        self.questions = self.ini.get_questions()
        self.dataset_preview = self.ini.get_dataset_prev()
        self.field_preview = self.ini.get_field_prev()
        self.modify_persona = utils.load_prompts(query="MODIFY_PROMPT")
        self.chart_desc_persona = utils.load_prompts(query="DESCRIPTION_PROMPT")
        self.chart_desc_with_instr_persona = utils.load_prompts(query="DESCRIPTION_PROMPT_WITH_COMMAND")
        self.quiz_desc_persona = utils.load_prompts(query="QUIZ_DESCRIPTION")

    def get_questions(self) -> dict:
        desc = []
        for q in self.questions:
            desc.append(self.generate_quiz_description(q))
        return {"questions": self.questions, "explanations": desc}

    def get_preview(self) -> str:
        return self.dataset_preview

    def get_sample(self, sample_data):
        self.sample = sample_data

    def update_questions(self, q: List[str]):
        self.questions = q

    def add_question(self, q: str):
        self.questions.append(q)

    def generate_charts_ini(self) -> None:
        self.charts = []
        for q in self.questions:
            self.generate_charts_user(q)

    def generate_charts_user(self, q: str) -> None:
        res = self.ini.generate(q)
        for ch in res:
            ch['question'] = q
            self.charts.append(ch)

    # Todo: each time adding new charts we should render again

    def modify_charts(self, target_chart: dict, user_input) -> dict:
        # Todo: data?
        # 让generator返回"vega-lite_code""explanation" 已完成
        prev_chart = target_chart
        # prev_question = target_chart.get("question")
        print(target_chart)
        print(user_input)
        modify_instr = "Here are the Vega_Lite charts that need to be modified:" + str(prev_chart) + "Here are the " \
                                                                                                "user-specified " \
                                                                                                "modification " \
                                                                                                "suggestions:" + \
                       user_input + "Please generate new charts and descriptions according to the given rules"

        generator = TextGen.TextGenerator()
        gpt_output: dict = generator.generate(self.modify_persona, modify_instr)

        new_chart = gpt_output.get("vega-lite_code")
        new_explanation = gpt_output.get("explanation")
        res_dic = {"vega-lite_code": new_chart, "explanation": new_explanation}  # , "question": prev_question}
        return res_dic

    def generate_chart_description(self, design_attr: str):
        """
        generate charts and description with design attribute and field description.
        :param design_attr: design attribute
        :return: dict {“explanations”:[], “codes”:[]}
        """
        instr = "Here is the chart:" + design_attr + "Here is the description of the dataset:" + self.dataset_preview + " and here is the description of the data attributes: " + str(
            self.field_preview) + " Here is the sample data:" + str(self.sample)
        generator = TextGen.TextGenerator()
        gpt_output: dict = generator.generate(self.chart_desc_persona, instr)
        return gpt_output

    def generate_chart_description_with_instr(self, design_attr: str, user_instr: str):
        """
        generate charts and description with design attribute and field description and user input.
        :param design_attr: design attribute
        :param user_instr: user command
        :return: dict {“explanations”:[], “codes”:[]}
        """
        instr = "Here is the chart:" + design_attr + " Here is the description of the dataset:" + self.dataset_preview + " here is the description of the data attributes(fields): " + str(
            self.field_preview) + " and this is what the user wants the chart to explain: " + user_instr

        generator = TextGen.TextGenerator()
        gpt_output: dict = generator.generate(self.chart_desc_with_instr_persona, instr)
        return gpt_output

    def generate_quiz_description(self, quiz: str):
        """
        :param quiz: the question
        :return: the description
        """
        if self.question_expls.get(quiz) is None:
            instr = "Here is the question:" + quiz + " here is the description of the data attributes(fields): " + str(
                self.field_preview)
            generator = TextGen.TextGenerator()
            gpt_output: dict = generator.generate(self.quiz_desc_persona, instr)
            self.question_expls[quiz] = gpt_output.get('description')
        return self.question_expls[quiz]

    def get_field(self) -> list:
        return list(self.field_preview.keys())