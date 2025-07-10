import pandas as pd
import execute_prompt as ep


# return f"no: {result["yes"]}" if result["yes"] > result["no"] else f"no: {result["no"]}"


def run(model : dict, verifies_rows : pd, primary_classified : str):
        rows = convertion_df_to_dict_into_list(verifies_rows)
        result = check_rows(model, rows, primary_classified)
        precent = f"{result / len(verifies_rows)*100}%"
        print(precent)
        return precent
def convertion_df_to_dict_into_list(verifies_rows : pd):
        rows = []
        for _,row in verifies_rows.iterrows():
                d = row.to_dict()
                rows.append(d)
        return rows

def check_rows(model : dict ,rows : list, primary_classified : str):
        successed = 0
        sum = 0
        for row in rows:
                sum += 1
                excepted = excepted_result(row, primary_classified)
                edited_row = row.copy()
                del edited_row[primary_classified]
                result = ep.execute(model, primary_classified, **edited_row)
                successed += 1 if result == excepted else 0
        return successed

def _result(row : dict, primary_classified : str):
        return row[primary_classified]