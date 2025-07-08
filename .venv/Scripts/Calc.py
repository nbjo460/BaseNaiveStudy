import pandas as pd

def run(table : pd, **kwargs):
    validate(table, **kwargs)
    Px = get_all_Px(table)
    result = get_Pxc(Px, age = "youth", income = "medium", student = "no", credit_rating = "fair")
    print(result)

    pc_yes = get_Pc(table, "yes")
    pc_no = get_Pc(table, "no")

    result["no"] *= pc_no
    result["yes"] *= pc_yes

    print(result)

def validate(table : pd, **kwargs):
    columns = table.columns.tolist()
    # print(columns)
    for arg in kwargs.keys():
        if arg not in columns:
            raise "Argument dosen't exist"

def get_all_Px(table : pd):
    # a = get_spesificly_Px(table, left_column_name="a",left_value= "a1", right_column_name = "exist", right_value= "yes")

    uniques = {}
    yes = {}
    no = {}
    for col in table.columns:
        if col == "exist": continue
        uniques[col] = table[col].unique()

    for col,val in uniques.items():
        if col not in yes:
            yes[col] = {}
        if col not in no:
            no[col] = {}

        for v in val:
            yes[col][v] = get_spesificly_Px(table, left_column_name = col, left_value = v, right_column_name = "exist", right_value = "yes")
            no[col][v] = get_spesificly_Px(table, left_column_name = col, left_value = v, right_column_name = "exist", right_value = "no")

    Px = {"yes" : yes, "no" : no}
    return Px

def get_Pc(table : pd, choice : str):
    return len(table[table["exist"] == choice]) /len(table)

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

# data = {"a":{1:"a1", 2:"a2", 3:"a3", 4:"a4"}, "b":{1:"b1", 2:"b2", 3:"b3", 4:"b4"},
#         "c":{1:"c1", 2:"c2", 3:"c3", 4:"c4"}, "exist":{1:"yes", 2:"yes", 3:"no", 4:"yes"}}
# df = pd.DataFrame(data)
df = pd.read_csv("buy_computer_data.csv")
df = df.drop('id', axis = 1)
print(df)
run(df)

