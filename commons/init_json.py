from __future__ import annotations
from dataclasses import dataclass
import json


@dataclass
class TestsData:
    """
    Store the initial data for the test that reading from init.json config file.
    """
    url: str
    email: str
    password: str
    browser: str

    @staticmethod
    def load(path: str) -> TestsData:
        """
        load and read the file and
        return data object
        :param path: path to json file
        :return: object with the data
        :rtype: TestsData
        """
        with open(path, "r") as json_file:
            json_file = json.load(json_file)
        return TestsData(**json_file)
