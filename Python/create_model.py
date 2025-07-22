import pandas as pd
from Python import execute_prompt
from Python import verify as vf
import Python.create_table
import numpy as np

from Python.create_table import create_table
from Python.training import train as tr


def run(file_name : str, primary_classified : str, drops : list, runner_platform):
    model, verifies_rows, table = creates_model(file_name, primary_classified, drops, runner_platform)
    probabillity = {"Px" : model, "Pc" : get_Pc(table, primary_classified, model.keys())}
    verify(probabillity, table, primary_classified)
    return probabillity

def creates_model(file_name : str, primary_classified : str, drops : list, runner_platform):
    table = get_table(file_name, drops, runner_platform)
    table = shuffle(table)
    dfs = split_table(table)

    # model = tr.trainer(dfs["train"], primary_classified)
    model = tr.trainer(get_table(file_name, drops, runner_platform), primary_classified)
    return model, dfs["verify"], table

def get_table(file_name : str, drops : list, runner_platform):
    ct = create_table()
    table = ct.create(file_name, runner_platform)
    table = drop_cols_by_ignore_list(table, drops)
    return table

def drop_cols_by_ignore_list(table : pd, drops : list):
    for index in drops:
        try:
            table = table.drop(index, axis=1)
        except Exception as e :
            print("can't drop index: " + e.__str__())
    return table

def get_Pc(table: pd, primary: str, classified : list):
    classes = {}
    for cls in classified:
        classes[cls] = len(table[table[primary] == cls]) / len(table)
    return classes

def split_table(table : pd):
    length = len(table)
    training_precent = int(length * 0.7)

    df1 = table[:training_precent]
    df2 = table[training_precent:]
    return {"train" : df1, "verify" : df2}

def shuffle(table : pd):
    return table.sample(frac  = 1).reset_index(drop=True)

def verify(model : dict, verifies_rows : pd,primary_classified : str):
    vf.run(model, verifies_rows, primary_classified)
