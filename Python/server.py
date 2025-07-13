import Python.create_model as cm
import Python.execute_prompt as pt

class Server:
    models = {}
    def __init__(self):
        pass
    def run_server(self, file_name : str, primary_classified : str, index : str, **kwargs):
        global models
        if file_name not in self.models:
            model = cm.run(file_name, primary_classified, index)
            self.models[file_name] = (model, primary_classified)
            print("New model created" + file_name)
        result = self.execute_for_server(self.models[file_name][0], self.models[file_name][1], **kwargs)
        print(self.models)
        return result

    def execute_for_server(self, model, primary_classified, **kwargs):
        result = pt.execute(model, primary_classified, **kwargs)
        return result