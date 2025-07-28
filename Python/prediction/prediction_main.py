import Python.models.prompt as prompt
from Python.models.model import Model
from Python.utils.execute_prompt import execute
import requests

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
        tmp_type_model = local_model.model_type
        if tmp_type_model not in Model.models:
            local_model = self._fetch_model(_prompt)
        else:
            local_model = Model.models[local_model.model_type]
        return local_model


    @staticmethod
    def _fetch_model(_prompt : prompt):
        model = Model.convert_prompt_to_model(_prompt)
        type_model = model.model_type
        # predict_model = requests.get(f"localhost:8010/get_model/{type_model.model_type.__str__()}")
        # model = Calc_main.get_model(model)
        response = requests.post(f"http://generate_model:8030/get_model/", json=type_model.__dict__)
        dict_model = response.json()
        model = Model(**dict_model)
        model.insert_self()
        return model


    def _create_json(self, data_name : str, model : dict):
        pass

# pt = Prompt("buy_computer_data", "exist", ["id"])
# print(Prediction_main().predict_with_model(pt))
