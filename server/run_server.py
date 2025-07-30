import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from Python.calculate_model.create_table import create_table as ct
from Python.utils.properties import properties_of_runner
from Python.utils.server import Server

app = FastAPI()
server = Server()

runner_platform = "main" if (__name__ == "__main__") else "server"

templates = Jinja2Templates(directory=properties_of_runner(runner_platform, "templates"))
app.mount("/static", StaticFiles(directory=properties_of_runner(runner_platform, "static")), name="static")

def list_csv_files(csv_folder : str):
    def find_csv_dir(start_path):
        current_path = os.path.abspath(start_path)
        while True:
            possible_csv = os.path.join(current_path, "csv")
            if os.path.isdir(possible_csv):
                return possible_csv
            parent = os.path.dirname(current_path)
            if parent == current_path:
                # הגענו לשורש ואין תיקיית csv
                raise FileNotFoundError("Could not find 'csv' directory")
            current_path = parent

    # תחילת החיפוש מהתיקייה של הסקריפט או מה-cwd
    csv_dir = find_csv_dir(os.getcwd())

    files_list = []
    for root, dir, files in os.walk(csv_dir):
        for file in files:
            if file[-4:].lower() == ".csv":
                files_list.append(file[:-4])

    return files_list


@app.get("/favicon.ico")
async def favicon():
    return None

@app.get("/", response_class= HTMLResponse)
def show_csv_list():
    names = list_csv_files(properties_of_runner(runner_platform, "csv"))
    html_buttons = "".join([
        f'<form action="/{name}" method="get" style="display:inline;"><button>{name}</button></form>'
        for name in names
    ])
    return f"""
<html>
<body>
<h1>TABLES</h1>
{html_buttons}
</body>
</html>
            """

@app.get("/{file_name}",response_class = HTMLResponse)
def get_absolute_route(file_name, request : Request):
    # try:
        drops, cols = create_dropdown(file_name)
        return templates.TemplateResponse("table_show.html",
                                          {"request":request, "table_name":file_name, "uniques" : drops,"cols" : cols})
    # except Exception as e:
    #     return f"No table: {file_name}\n {e}"

@app.get("/calculate_model/{file_name}/{primary}/{index}/{keys:path}", response_class = HTMLResponse)
def get_prediction(file_name ,primary : str, index : str, keys : str):
    pairs = keys.split("/")
    params = {}
    # file_name = get_absolute_name(file_name)
    for pair in pairs:
        if '=' in pair:
            tmp = pair.split("=", 1)
            params[tmp[0]] = tmp[1] if tmp[1] != "" else "Empty"
    index = index.split(",")
    result = server.run_server(file_name, primary, index, **params, runner_platform=runner_platform)
    return f"<h2>Prediction result:</h2><p>The result is:{result[0]}.<br>by {result[1]*100:.2f}%</p>"
    # return result

@app.post("/calculate_model/{file_name}/{keys:path}")
async def post_prediction(file_name, request : Request, keys:str):
    params = dict(await request.json())

    sel = params["selects"]
    drops = params["drops"]
    classified = params["classified"]
    result = server.run_server(file_name, classified, drops, runner_platform, **sel)
    return {"result": result}

def create_dropdown(file_name):
    uniques = {}
    a = ct()
    df = a.create(file_name, runner_platform)
    cols = df.columns.tolist()
    for col in cols:
        uniques[col] = df[col].unique().tolist()
    return uniques,cols


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8001)
