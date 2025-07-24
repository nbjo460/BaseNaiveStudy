from Python.models.prompt import Prompt


class Model:
    models = {}
    def __init__(self, _data_file_name : str, _ignore_cols : list,  _classified_by : str):
        self.data_file_name = _data_file_name
        self.ignore_cols = _ignore_cols
        self.classified_by = _classified_by
        self.succeed_level = 0
        self.naive_base_model = {}


    def get_succeed_level_percent(self):
        return str(self.succeed_level) + "%"

    def insert_self(self):
        model_key = Model.get_type_of_model(self.data_file_name, self.classified_by, self.ignore_cols)
        if model_key not in Model.models:
            Model.models[model_key] = self

    def _create_model_dict(self):
        raise "no finish _create_model_dict() func"

    @staticmethod
    def get_type_of_model(_data_name: str, _classified_by: str, _ignore_cols: list):
        _ignore_cols = tuple(_ignore_cols)
        return _data_name, _classified_by, _ignore_cols

    @staticmethod
    def get_type_of_model_by_class(model):
        tmp_ignore_cols = tuple(model.ignore_cols)
        tmp_tuple = model.data_file_name, model.classified_by, tmp_ignore_cols
        return tmp_tuple

    @staticmethod
    def convert_prompt_to_model(_prompt : Prompt):
        return Model(_data_file_name = _prompt.data_file_name, _ignore_cols=_prompt.ignore_cols, _classified_by =_prompt.classified_by)

