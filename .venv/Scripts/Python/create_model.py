import pandas as pd
import execute_prompt
import verify as vf
from training import train as tr


def run(file_name : str, primary_classified : str):
    model, verifies_rows, table = creates_model(file_name, primary_classified)
    probabillity = {"Px" : model, "Pc" : get_Pc(table, primary_classified, model.keys())}
    verify(probabillity, table, primary_classified)
    return probabillity

def creates_model(file_name : str, primary_classified : str):
    table = get_table(file_name)
    table = shuffle(table)
    dfs = split_table(table)

    model = tr.trainer(dfs["train"], primary_classified)
    # model = tr.trainer(get_table(file_name), primary_classified)
    return model, dfs["verify"], table

def get_table(file_name : str):
    table = pd.read_csv(file_name)
    table = table.drop("Index", axis=1)
    return table

def get_Pc(table: pd, primary: str, classified : list):
    classes = {}
    for cls in classified:
        classes[cls] = len(table[primary] == cls) / len(table)
    return classes

def split_table(table : pd):
    length = len(table)
    training_precent = int(length * 0.7)
    print(training_precent)

    df1 = table[:training_precent]
    df2 = table[training_precent:]
    return {"train" : df1, "verify" : df2}

def shuffle(table : pd):
    return table.sample(frac  =1, random_state=42).reset_index(drop=True)

def verify(model : dict, verifies_rows : pd,primary_classified : str):
    vf.run(model, verifies_rows, primary_classified)
