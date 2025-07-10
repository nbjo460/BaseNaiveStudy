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
    Pxs = {}
    for cls in Px.keys():
        Pxs[cls] = 1

    for keys ,cls in Px.items():
        for col, value in cls.items():
            if col in kwargs: Pxs[keys] *= value
    return Pxs

def get_PxcPc(Pc : dict ,Pxc : dict, primary_classified : str):
    tmp = Pxc.copy()
    for cls in Pxc.keys():
        tmp[cls] *= Pc[cls]
    return Pxc

def calculate(Pc : dict, Px : dict, primary_classified : str, **kwargs):
    Pxc = get_Pxc(Px, **kwargs)
    PxcPc = get_PxcPc(Pc, Pxc, primary_classified)
    return PxcPc

def show_result(result : dict):
    return max(result.values())
