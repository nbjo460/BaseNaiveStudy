import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from Python.utils.properties import properties_of_runner

runner_platform = "main" if (__name__ == "__main__") else "server"

app = FastAPI()
app.mount("/static", StaticFiles(directory=properties_of_runner(runner_platform, "static")), name="static")

templates = Jinja2Templates(directory=properties_of_runner(runner_platform, "templates"))

@app.get("/favicon.ico")
async def favicon():
    return None

@app.get("/", response_class= HTMLResponse)
def show_csv_list():
    pass

@app.get("/add_csv")
def add_csv():
    pass
@app.get("/{file_name}",response_class = HTMLResponse)
def get_absolute_route(file_name, request : Request):
   pass

@app.get("/calculate_model/{file_name}/{primary}/{index}/{keys:path}", response_class = HTMLResponse)
def get_prediction(file_name ,primary : str, index : str, keys : str):
    pass

@app.post("/calculate_model/{file_name}/{keys:path}")
async def post_prediction(file_name, request : Request, keys:str):
   pass

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8001)
