import pandas as pd
import Python.properties
from Python.clean_table import clean as cl
from Python.properties import properties_of_runner


class create_table:
    tables = {}


    def create(self, file_name  :str, _runner_platform : str):
        if file_name not in self.tables:
            table = self.read_file(file_name, _runner_platform)
            table = self.clean(table)
            self.tables[file_name] = table
            return table
        return self.tables[file_name]

    @staticmethod
    def read_file(file_name, runner_platform):
        name = create_table.get_absolute_name(file_name, runner_platform)
        df = pd.read_csv(name)
        return df

    @staticmethod
    def clean(table : pd):
        table = table.drop_duplicates()
        table = cl(table)
        return table

    @staticmethod
    def get_absolute_name(file_name : str, _runner_platform):
        file_name = file_name.strip()
        return properties_of_runner(_runner_platform, "csv") + file_name + ".csv"
