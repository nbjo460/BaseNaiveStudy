import pandas as pd


def clean(table:pd):
    table = drop_uniques(table)
    table = table.astype(str)
    return table

def drop_uniques(table : pd):
    cols = table.columns
    for col in cols:
        if table[col].is_unique:
            table = table.drop(col, axis = 1)
    return table

