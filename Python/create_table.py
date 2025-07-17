import pandas as pd
from Python.clean_table import clean as cl


class create_table:
    tables = {}


    def create(self, file_name  :str):
        if file_name not in self.tables:
            table = self.read_file(file_name)
            table = self.clean(table)
            self.tables[file_name] = table
            return table
        return self.tables[file_name]

    @staticmethod
    def read_file(file_name):
        name = create_table.get_absolute_name(file_name)
        df = pd.read_csv(name)
        return df

    @staticmethod
    def clean(table : pd):
        table = table.drop_duplicates()
        table = cl(table)
        return table

    @staticmethod
    def get_absolute_name(file_name : str):
        file_name = file_name.strip()
        return "../csv/" + file_name + ".csv"
