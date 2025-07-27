from pathlib import Path


def properties_of_runner(runner_platform: str, req_path: str):
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    python_root = PROJECT_ROOT

    pathes = {
        "server": {
            "csv": python_root / "csv",
            "templates": python_root / "templates",
            "static": python_root / "static"
        },
        "main": {
            "csv": python_root / "csv",
            "templates": python_root / "templates",
            "static": python_root / "static"
        }
    }

    return str(pathes[runner_platform][req_path])+"/"
