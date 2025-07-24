def properties_of_runner(runner_platform : str, req_path : str):
    pathes = {
            "server":{"csv":"/app/csv/", "templates":"/app/templates", "static":"/app/static"},
            "main":{"csv":"../../csv/", "templates":"../templates", "static":"../static"}
              }
    return pathes[runner_platform][req_path]
