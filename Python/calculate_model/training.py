import pandas as pd
import json
import numpy as np
class train:

    @staticmethod
    def trainer(table : pd, primary_classified : str):
        Px = train.get_all_Px(table, primary_classified)
        train.save_json(Px)
        return Px

    @staticmethod
    def get_all_Px(table : pd, primary : str):
        uniques, classified = train.create_unique_in_col(table, primary)
        types_class = {}

        for cls in classified:
            # cls = str(cls)
            types_class[cls] = {}
            for col,val in uniques.items():
                # col = str(col)
                bug = train.get_zero_bug_cols(table, uniques, col, primary, cls)
                for v in val:
                    # v = str(v)
                    if col not in types_class[cls]: types_class[cls][col] = {}

                    types_class[cls][col][v] = train.get_spesificly_Px(table, left_column_name=col, left_value=v, right_column_name=primary,
                                            right_value = cls, zero_bug=bug)
        return types_class

    @staticmethod
    def create_unique_in_col(table : pd, primary : str):
        uniques = {}
        classified = table[primary].unique().tolist()
        for col in table.columns:
            if col == primary: continue
            uniques[col] = table[col].unique()
            # uniques[col] = table[col].unique().tolist()
            # print(type(uniques[col]))
        return uniques, classified

    @staticmethod
    def get_zero_bug_cols(table : pd, uniques :dict , col : str, primary : str, cls :str):
        classes = table[table[primary] == cls]
        num = classes[col].nunique()
        all = len(uniques[col])

        return num < all

    @staticmethod
    def get_spesificly_Px(table: pd, right_column_name : str, right_value : str, left_column_name : str, left_value : str, zero_bug : bool, k=1):

        right_table = table[table[right_column_name] == right_value]

        right_count = len(right_table)
        left_count = len(right_table[right_table[left_column_name] == left_value])
        return left_count / right_count if not zero_bug else (left_count+1) /(right_count+1)

    @staticmethod
    def save_json(Px : dict):
        Px = train.convert_keys(Px)
        with open("../buy_computer_data.json", "w") as outfile:
            json.dump(Px, outfile)

    @staticmethod
    def convert_keys(d):
        if isinstance(d, dict):
            return {int(k) if isinstance(k, (np.integer,)) else k: train.convert_keys(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [train.convert_keys(i) for i in d]
        else:
            return d
