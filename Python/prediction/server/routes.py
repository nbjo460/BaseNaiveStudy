import fastapi
import uvicorn
import Python.prediction.server.background_server as back
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from Python.utils.properties import properties_of_runner


class Routes:
    app = fastapi.FastAPI()
    app.mount("/static", StaticFiles(directory=properties_of_runner("server", "static")), name="static")
    templates = Jinja2Templates(directory=properties_of_runner("server", "templates"))

    def __init__(self):
        pass


    @staticmethod
    @app.get("/micro_service/{file_name}/{classified_by}/{keys:path}")
    def micro_service(request : fastapi.Request, keys : str, classified_by : str, file_name : str,ignore_by : str = fastapi.Query(default=""), parameters : str = fastapi.Query(default="")):
            return back.micro_service(keys,classified_by,file_name,ignore_by, parameters)
if __name__ =="__main__":
    uvicorn.run(Routes.app, host="localhost", port=8020)