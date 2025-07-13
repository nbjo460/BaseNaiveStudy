import pandas as pd
from training import train as tr
import numpy as np

def execute(model : dict ,primary_classified : str ,**kwargs):
    Px = model["Px"]
    Pc = model["Pc"]
    result = calculate(Pc, Px, primary_classified, **kwargs)
    result = show_result(result)
    return result

def get_Pxc(Px, **kwargs):
    pxc = {}
    for cls in Px.keys():
        pxc[cls] = 1
    for cls in Px:
        for col ,val in kwargs.items():
            if col in Px[cls]:
                try:
                    pxc[cls] *= Px[cls][col][val]
                except:
                    print(f"I dont have enough data of: {val}")
    return pxc

def get_PxcPc(Pc : dict ,Pxc : dict, primary_classified : str):
    tmp = Pxc.copy()
    for col in Pc.keys():
            tmp[col] *= Pc[col]
    return tmp

def calculate(Pc : dict, Px : dict, primary_classified : str, **kwargs):
    Pxc = get_Pxc(Px, **kwargs)
    PxcPc = get_PxcPc(Pc, Pxc, primary_classified)
    return PxcPc

def show_result(result : dict):
    max_name = ""
    max_value = 0
    for name, value in result.items():
        if value > max_value:
            max_name = name
            max_value = value
    return max_name
