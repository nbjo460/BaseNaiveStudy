import pandas as pd
from training import train as tr

# def execute(table : pd, primary_classified : str ,**kwargs):
def execute(model : dict ,primary_classified : str ,**kwargs):
    Px = model["Px"]
    Pc = model["Pc"]
    # Pc = get_Pc(table, primary_classified)
    # Px = tr.trainer(table, primary_classified)
    # result = calculate(Pc, Px, primary_classified, **kwargs)
    result = calculate(Pc, Px, primary_classified, **kwargs)
    return result

def get_Pxc(Px, **kwargs):
    no = Px["no"]
    yes = Px["yes"]

    num_no = 1
    num_yes = 1
    for col, value in no.items():
        if col in kwargs: num_no *= value[kwargs[col]]

    for col, value in yes.items():
        if col in kwargs: num_yes *= value[kwargs[col]]

    result = {"no" : num_no, "yes" : num_yes}
    return result

# def get_Pc(table : pd, primary : str):
#      yes = len(table[table[primary] == "yes"]) /len(table)
#      no = len(table[table[primary] == "no"]) /len(table)
#      return {"yes" : yes, "no" : no}

def get_PxcPc(Pc : dict ,Pxc : dict, primary_classified : str):
    Pxc["no"] *= Pc["no"]
    Pxc["yes"] *= Pc["yes"]

    return Pxc

def calculate(Pc : dict, Px : dict, primary_classified : str, **kwargs):
    Pxc = get_Pxc(Px, **kwargs)
    PxcPc = get_PxcPc(Pc, Pxc, primary_classified)
    return PxcPc