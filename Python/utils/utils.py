# find if data (model, json) are exists
# convert json to data
# convert data to json
import json
import os.path
import Python.models.model
from Python.models.model import Model


# def get_model(_data_file_name : str, _classified_by : str, _ignore_cols : list):
#     return Model(_data_file_name = _data_file_name, _classified_by= _classified_by, _ignore_cols=_ignore_cols)

def convert_json_to_dict(path):
    return json.loads(path)

def convert_dict_to_json(path, name):
    pass

def _is_exist_json_locally(path, file_name):
    full_path = full_path_merge(path, file_name)
    return os.path.exists(full_path)


def full_path_merge(path, file_name):
    return os.path.join(path, file_name)