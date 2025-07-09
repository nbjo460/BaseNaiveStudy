import pandas as pd
import json
import numpy as np
class train:

    @staticmethod
    def trainer(table : pd, primary_classified : str):
        Px = train.get_all_Px(table, primary_classified)
        train.save_json(Px)
        print(Px)
        return Px

    @staticmethod
    def get_all_Px(table : pd, primary : str):
        uniques = train.create_unique_in_col(table, primary)
        yes = {}
        no = {}

        for col,val in uniques.items():
            yes[col] = {}
            no[col] = {}

            for v in val:
                yes_len = len(table[(table[primary] == "yes") & (table[col] == v)])
                no_len = len(table[(table[primary] == "no") & (table[col] == v)])

                yes_zero = yes_len < 1
                no_zero = no_len < 1

                yes[col][v] = train.get_spesificly_Px(table, left_column_name = col, left_value = v, right_column_name = primary, right_value = "yes", zero_bug = yes_zero, k = yes_len)
                no[col][v] = train.get_spesificly_Px(table, left_column_name = col, left_value = v, right_column_name = primary, right_value = "no", zero_bug = no_zero, k = no_len)

        Px = {"yes" : yes, "no" : no}

        return Px

    @staticmethod
    def create_unique_in_col(table : pd, primary : str):
        uniques = {}
        for col in table.columns:
            if col == primary: continue
            uniques[col] = table[col].unique()
        return uniques

    @staticmethod
    def avoid_zero_bug():
        pass
    @staticmethod
    def get_spesificly_Px(table: pd, right_column_name : str, right_value : str, left_column_name : str, left_value : str, zero_bug : bool, k=1):

        right_table = table[table[right_column_name] == right_value]

        right_count = len(right_table)
        left_count = len(right_table[right_table[left_column_name] == left_value])


        return left_count / right_count if not zero_bug else (left_count+1) /(right_count+k)

    @staticmethod
    def save_json(Px : dict):
        Px = train.convert_keys(Px)
        with open("buy_computer_data.json", "w") as outfile:
            json.dump(Px, outfile)

    @staticmethod
    def convert_keys(d):
        if isinstance(d, dict):
            return {int(k) if isinstance(k, (np.integer,)) else k: train.convert_keys(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [train.convert_keys(i) for i in d]
        else:
            return d
