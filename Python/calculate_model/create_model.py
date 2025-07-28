# import traceback

import pandas as pd

from Python.calculate_model.create_table import create_table
from Python.calculate_model.training import train as tr

class Create_model:
    @staticmethod
    def run(file_name : str, primary_classified : str, drops : list, runner_platform):
        model, verifies_rows, table = Create_model.creates_model(file_name, primary_classified, drops, runner_platform)
        calculate_model = {"Px" : model, "Pc" : Create_model.get_Pc(table, primary_classified, model.keys())}
        percent = Create_model.verify(calculate_model, table, primary_classified)
        return calculate_model, percent

    @staticmethod
    def creates_model(file_name : str, primary_classified : str, drops : list, runner_platform):
        table = Create_model.get_table(file_name, drops, runner_platform)
        table = Create_model.shuffle(table)
        dfs = Create_model.split_table(table)

        # calculate_model = tr.trainer(dfs["train"], primary_classified)
        calculate_model = tr.trainer(table, primary_classified)
        return calculate_model, dfs["verify"], table

    @staticmethod
    def get_table(file_name : str, drops : list, runner_platform):
        ct = create_table()
        table = ct.create(file_name, runner_platform)
        table = Create_model.drop_cols_by_ignore_list(table, drops)
        return table

    @staticmethod
    def drop_cols_by_ignore_list(table : pd, drops : list):
        for index in drops:
            try:
                table = table.drop(index, axis=1)
            except Exception as e :
                # traceback.print_stack(limit=3)  # מראה 3 שלבים אחורה
                print("can't drop index: " + e.__str__())
        return table

    @staticmethod
    def get_Pc(table: pd, primary: str, classified : list):
        classes = {}
        for cls in classified:
            classes[cls] = len(table[table[primary] == cls]) / len(table)
        return classes

    @staticmethod
    def split_table(table : pd):
        length = len(table)
        training_precent = int(length * 0.7)

        df1 = table[:training_precent]
        df2 = table[training_precent:]
        return {"train" : df1, "verify" : df2}

    @staticmethod
    def shuffle(table : pd):
        return table.sample(frac  = 1).reset_index(drop=True)

    @staticmethod
    def verify(model : dict, verifies_rows : pd,primary_classified : str):
        from Python.calculate_model import verify as vf

        return vf.run(model, verifies_rows, primary_classified)
