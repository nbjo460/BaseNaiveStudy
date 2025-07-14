import os

import fastapi
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from Python.server import Server
import pandas as pd

app = FastAPI()
server = Server()

def list_csv_files(csv_folder : str):
    files_list = []
    for root, dir, files in os.walk(csv_folder):
        for file in files:
            if file[-4:].lower() == ".csv":
                files_list.append(file[:-4])

    return files_list

@app.get("/", response_class= HTMLResponse)
async def show_csv_list():
    names = list_csv_files("../csv")
    html_buttons = "".join([
        f'<form action="/{name}" method="get" style="display:inline;"><button>{name}</button></form>'
        for name in names
    ])
    return f"""
<html>
<body>
<h1>buttons</h1>
{html_buttons}
</body>
</html>
            """

@app.get("/{file_name}",response_class = HTMLResponse)
def get_absolute_route(file_name):
    try:
        file_name = file_name.strip()
        absolute_name = get_absolute_name(file_name)
        with open(absolute_name, "r") as f:
            columns_names = f.readline()
            columns_splitted = columns_names.strip().split(',')
            index_route = columns_splitted[0]
            primary_cls = columns_splitted[-1]
            columns_splitted = columns_splitted[1:-1]
            columns_shows = ' ,'.join(columns_splitted)
            end = "=XXX"
            columns_routes = f"prediction/{file_name}/{index_route}/{primary_cls}/{f"{end}/".join(columns_splitted)}{end}"
        out = (f"The table is: {file_name}. <br>"
               f"The columns are:<br>{columns_shows}.<br>"
               f'<a href="/{columns_routes}" style="margin: 10px; display: inline-block; color:red; font-size : 20px;">{columns_routes}</a>')
        drops = create_dropdown(absolute_name, primary_cls, index_route)
        return out + drops
    except:
        return f"No table: {file_name}"

@app.get("/prediction/{file_name}/{primary}/{index}/{keys:path}", response_class = HTMLResponse)
def get_prediction(file_name ,primary : str, index : str, keys : str):
    pairs = keys.split("/")
    params = {}
    file_name = get_absolute_name(file_name)
    for pair in pairs:
        if '=' in pair:
            tmp = pair.split("=", 1)
            params[tmp[0]] = tmp[1] if tmp[1] != "" else "Empty"
    result = server.run_server(file_name, index, primary, **params)
    return f"<h2>Prediction result:</h2><p>The result is:{result[0]}.<br>by {result[1]*100:.2f}%</p>"

def create_dropdown(file_name, primary, index):
    uniques = {}
    df = pd.read_csv(file_name)
    df = df.drop_duplicates()
    df = df.drop(index, axis = 1)
    df = df.drop(primary, axis = 1)
    cols = df.columns
    for col in cols:
        uniques[col] = df[col].unique().tolist()

    html = '<form method = "post">'
    for col, unique in uniques.items():
        html += f"""
                    <label for="dropdown{col}"> {col}</label>
                    <select name="dropdown{col}" id="dropdown{col}">
                    """
        for uni in unique:
            html+= f"""<option value="{col}-{uni}">{col}-{uni}</option>"""
        html+="""</select>
                    <br>
                """
    return html
def get_absolute_name(file_name : str):
    return "../csv/" + file_name + ".csv"


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8001)