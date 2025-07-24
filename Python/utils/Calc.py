import pandas as pd
from Python.prediction import execute_prompt


def run(table : pd, primary_classified : str, **kwargs):
    validate(table, **kwargs)
    result = execute_prompt.execute(table, primary_classified, **kwargs)
    normal_result = normalization(result)
    print(normal_result)


def validate(table : pd, **kwargs):
    columns = table.columns.tolist()
    # print(columns)
    for arg in kwargs.keys():
        if arg not in columns:
            raise ValueError ("Argument dosen't exist")

def normalization(PxcPc : dict):
    total = PxcPc["yes"] + PxcPc["no"]
    PxcPc["yes"] /= total
    PxcPc["no"] /= total
    return PxcPc



df = pd.read_csv("buy_computer_data.csv")
df = df.drop('id', axis = 1)
print(df)
run(df, "exist", age = "youth", income = "medium", student = "no", credit_rating = "fair")

