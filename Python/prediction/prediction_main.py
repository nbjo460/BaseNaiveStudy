import Python.models.prompt as prompt
from Python.calculate_model.calc_main import Calc_main
from Python.models.model import Model
from Python.prediction.execute_prompt import execute


class Prediction_main:
    def __init__(self):
        pass

    def predict_with_model(self, _prompt : prompt, **_parameters):
        model = self._load_model(_prompt)
        prediction = execute(model.naive_base_model, model.classified_by, **_parameters)
        return prediction

    def get_bulk_prompts(self, _prompts : list):
        # using model to calc a result
        # return a result
        pass

    def _load_model(self, _prompt : prompt):
        local_model = Model.convert_prompt_to_model(_prompt)
        tmp_type_model = Model.get_type_of_model_by_class(local_model)
        if tmp_type_model not in Model.models:
            local_model = self._fetch_model(_prompt)
        else:
            local_model = Model.models[Model.get_type_of_model_by_class(local_model)]
        return local_model


    @staticmethod
    def _fetch_model(_prompt : prompt):
        model = Model.convert_prompt_to_model(_prompt)
        type_model = Model.get_type_of_model_by_class(model)
        predict_model = Calc_main.get_model(type_model)
        model.naive_base_model = predict_model
        model.insert_self()
        return model

    def _join_model_to_existing_json(self):
        pass
    def _create_json(self, data_name : str, model : dict):
        pass

# pt = Prompt("buy_computer_data", "exist", ["id"])
# print(Prediction_main().predict_with_model(pt))