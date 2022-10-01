# -*- coding: utf-8 -*-
import yaml

from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            self.students = yaml.load(file, Loader=yaml.Loader)
        return self.students
