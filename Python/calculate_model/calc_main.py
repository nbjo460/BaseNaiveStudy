from Python.calculate_model.create_model import Create_model
from Python.models.model import Model


class Calc_main:
    def __init__(self):
        pass
    @staticmethod
    def get_model(model_type):
        if model_type in Model.models:
            return Model.models[model_type]
        else:
            model = Create_model.run(model_type[0],model_type[1], model_type[2], "main")
            tmp_model = Model(model_type[0], _classified_by = model_type[1], _ignore_cols = model_type[2])
            tmp_model.naive_base_model = model
            tmp_model.insert_self()
            return model