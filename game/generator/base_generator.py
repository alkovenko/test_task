import json
from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    def __init__(self, json_file):
        self.data = self.load_data(json_file)

    def load_data(self, json_file):
        with open(json_file, "r", encoding="utf-8") as data:
            return json.load(data)

    @abstractmethod
    def generate(self):
        pass
