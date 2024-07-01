import MainProcessor
from MainProcessor import FileUploadProcessor
import unittest
import utils
import json

spec = utils.parse_specs()


class TestFix(unittest.TestCase):
    def test_1(self):
        sample = '''
            {
                "encoding": {
                    "y": {
                        "field": "Miles_per_Gallon",
                        "type": "quantitative"
                    },
                    "x": {
                        "field": "Year",
                        "type": "temporal",
                        "timeUnit": "year"
                    },
                    "color":{}
                },
                "mark": "point"
            }
            '''
        sample = json.loads(sample)
        res