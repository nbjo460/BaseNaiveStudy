import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from Python.calculate_model.calc_main import Calc_main
from Python.models.model import Model_type, Model
from Python.utils.properties import properties_of_runner


class Routes:
    app = fastapi.FastAPI()
    app.mount("/static", StaticFiles(directory=properties_of_runner("server", "static")), name="static")
    templates = Jinja2Templates(directory=properties_of_runner("server", "templates"))

    def __init__(self):
        pass

    @staticmethod
    @app.get("/")
    def root(request : fastapi.Request):
        a = {"request":request, "table_name":"file_name", "uniques" : {},"cols" : []}
        return {}

    @staticmethod
    @app.post("/get_model/")
    def micro_service(data : dict):
        model_type = Model_type(**data)
        model = Model(model_type.data_file_name, classified_by= model_type.classified_by, ignore_cols=model_type.ignore_cols)

        return Calc_main.get_model(model)
if __name__ =="__main__":
    uvicorn.run(Routes.app, host="localhost", port=8011)