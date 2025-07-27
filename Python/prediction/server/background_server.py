import fastapi
from Python.models.prompt import Prompt
from Python.prediction.prediction_main import Prediction_main


def micro_service(keys : str, classified_by : str, file_name : str,ignore_by : str = fastapi.Query(default="")):
    tmp_ignore_by = ignore_by.split(",")
    pairs = keys.split(",")
    params = {}
    for pair in pairs:
        splitted = pair.split("=")
        if len(splitted) > 1:
            params[splitted[0]] = splitted[1] if splitted[1] != "" else "Empty"
    p = Prompt(file_name, classified_by,tmp_ignore_by)
    r = Prediction_main().predict_with_model(p, **params)
    return r
