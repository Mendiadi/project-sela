from __future__ import annotations
from dataclasses import dataclass
import json


@dataclass
class TestsData:
    url: str
    email: str
    password: str
    browser: str

    @staticmethod
    def load(path: str) -> TestsData:
        with open(path, "r") as json_file:
            json_file = json.load(json_file)
        return TestsData(**json_file)
