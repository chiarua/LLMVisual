import openai
from openai import OpenAI
import json
import pandas as pd
import os
from . import utils

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

class TextGenerator:
    def __init__(self):
        self.client = OpenAI()

        self.prompts = utils.load_prompts()
        try:
            self.persona = utils.load_prompts(query='SUMMARIZE_PROMPT')
            self.instruction = utils.load_prompts(query='SUMMARIZE_INST')
        except KeyError as e:
            raise ValueError(f"Key {e} does not exist in the JSON file.")

    def generate(self, persona: str, instruction: str):
        """
        core method, return json object which can be dict as GPT's output
        :param persona: One of *model_prompts*
        :param instruction: as task description to specify the task, it should has unique information of given task
        :return: the *dict* which has dif
        """
        system_message = {"role": "system",
                          "content": instruction}
        client = self.client
        response = client.chat.completions.create(
            messages=[system_message, {"role": "user", "content": persona}],
            temperature=0.9,
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"}
        )
        json_str = response.choices[0].message.content
        # checking for small probability things
        if json_str[:6] == "```json":
            json_str = json_str.replace('```json', '').replace('```', '')
        # print("this is json_str:")
        # print(json_str)
        message = json.loads(json_str)

        return message

    def dataset_preview(self, dataset: str) -> dict:
        """
        :param dataset: a string including 7 cols of data
        :return: a dict with 'preview': {'name' 'dataset_description' 'field description' 'questions'}
        """
        persona = self.persona
        instruction = self.instruction + dataset
        dic = self.generate(persona, instruction)
        return dic

    def read_json(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        attributes = data.get('attributes', {})
        sample = data.get('data', [])[:7]
        df = pd.DataFrame(sample)
        columns = df.columns
        return ', '.join(columns)
