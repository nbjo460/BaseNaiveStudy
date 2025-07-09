import pandas as pd

def run(table : pd, primary_classified : str, **kwargs):
    validate(table, **kwargs)
    Px = get_all_Px(table, primary_classified)
    Pxc = get_Pxc(Px, **kwargs)
    PxcPc = get_PxcPc(table ,Pxc, primary_classified)

    normal_result = normalization(PxcPc)
    print(normal_result)


def validate(table : pd, **kwargs):
    columns = table.columns.tolist()
    # print(columns)
    for arg in kwargs.keys():
        if arg not in columns:
            raise ValueError ("Argument dosen't exist")

def get_all_Px(table : pd, primary : str):
    uniques = {}
    yes = {}
    no = {}
    for col in table.columns:
        if col == primary: continue
        uniques[col] = table[col].unique()

    for col,val in uniques.items():
        if col not in yes:
            yes[col] = {}
        if col not in no:
            no[col] = {}

        for v in val:
            yes[col][v] = get_spesificly_Px(table, left_column_name = col, left_value = v, right_column_name = primary, right_value = "yes")
            no[col][v] = get_spesificly_Px(table, left_column_name = col, left_value = v, right_column_name = primary, right_value = "no")

    Px = {"yes" : yes, "no" : no}
    return Px

def get_Pc(table : pd, choice : str, primary : str):
    return len(table[table[primary] == choice]) /len(table)

def get_spesificly_Px(table: pd, right_column_name : str, right_value : str,
    left_column_name : str, left_value : str):

    right_table = table[table[right_column_name] == right_value]

    right_count = len(right_table)
    left_count = len(right_table[right_table[left_column_name] == left_value])


    return left_count / right_count

def get_count_p(table : pd ,column : str):
    return table.groupby(column).count()

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

def get_PxcPc(table : pd ,Pxc : dict, primary_classified : str):
    pc_yes = get_Pc(table, "yes", primary_classified)
    pc_no = get_Pc(table, "no", primary_classified)

    Pxc["no"] *= pc_no
    Pxc["yes"] *= pc_yes

    return Pxc

def normalization(PxcPc : dict):
    total = PxcPc["yes"] + PxcPc["no"]
    PxcPc["yes"] /= total
    PxcPc["no"] /= total
    return PxcPc

df = pd.read_csv("buy_computer_data.csv")
df = df.drop('id', axis = 1)
print(df)
run(df, "exist", age = "youth", income = "medium", student = "no", credit_rating = "fair")

