import fastapi
from Python.models.prompt import Prompt
from Python.prediction.prediction_main import Prediction_main


def micro_service(keys : str, classified_by : str, file_name : str,ignore_by : str = fastapi.Query(default=""), parameters : str = fastapi.Query(default="")):
    ignore_by_list = ignore_by.split(",")
    pairs = parameters.split(",")
    params = {}
    for pair in pairs:
        splitted = pair.split("=")
        if len(splitted) > 1:
            params[splitted[0]] = splitted[1] if splitted[1] != "" else "Empty"
    p = Prompt(file_name, classified_by,ignore_by_list)
    r = Prediction_main().predict_with_model(p, **params)
    return r

