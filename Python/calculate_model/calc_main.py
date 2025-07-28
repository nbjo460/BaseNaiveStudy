from Python.calculate_model.create_model import Create_model
from Python.models.model import Model


class Calc_main:
    def __init__(self):
        pass
    @staticmethod
    def get_model(model : Model):
        if model.model_type in Model.models:
            return Model.models[model.model_type]
        else:
            calculate_model, percent = Create_model.run(model.data_file_name, model.classified_by, model.ignore_cols, "main")
            tmp_model = Model(data_file_name= model.data_file_name, classified_by = model.classified_by, ignore_cols = model.ignore_cols)
            tmp_model.succeed_level = percent
            tmp_model.naive_base_model = calculate_model
            tmp_model.insert_self()
            return tmp_model