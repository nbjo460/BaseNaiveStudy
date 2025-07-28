from Python.models.prompt import Prompt


class Model:
    models = {}
    def __init__(self, data_file_name : str, ignore_cols : list,  classified_by : str, naive_base_model: dict = {}, succeed_level = "", model_type = 0):
        self.data_file_name = data_file_name
        self.ignore_cols = ignore_cols
        self.classified_by = classified_by
        self.succeed_level = succeed_level
        self.naive_base_model = naive_base_model
        self.model_type = self._set_model_type()


    def get_succeed_level_percent(self):
        return str(self.succeed_level) + "%"

    def insert_self(self):
        if self.model_type not in Model.models:
            Model.models[self.model_type] = self

    def _create_model_dict(self):
        raise "no finish _create_model_dict() func"

    def _set_model_type(self):
        return Model_type(self.data_file_name, classified_by = self.classified_by, ignore_cols = self.ignore_cols)

    @staticmethod
    def convert_prompt_to_model(_prompt: Prompt):
            return Model(data_file_name=_prompt.data_file_name, ignore_cols=_prompt.ignore_cols,
                         classified_by=_prompt.classified_by)

    def __str__(self):
        self.model_type.__str__()

class Model_type:
    def __init__(self,  data_file_name : str, ignore_cols : list,  classified_by : str):
        self.data_file_name = data_file_name
        self.ignore_cols = ignore_cols
        self.classified_by = classified_by


    def get_type_of_model(self):
            self.ignore_cols = tuple(self.ignore_cols)
            return self.data_file_name, self.classified_by, self.ignore_cols

    def __str__(self):
        def ignore_to_list():
            return ",".join(self.ignore_cols)
        ignore = f"?ignore_by={ignore_to_list()}"
        classified = f"?classified_by={self.classified_by}"
        name=f"?data_file_name={self.data_file_name}"
        return ignore+classified+name