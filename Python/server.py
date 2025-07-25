import Python.create_model as cm
import Python.execute_prompt as pt

class Server:
    models = {}
    def __init__(self):
        pass
    def run_server(self, file_name : str, primary_classified : str, drops : list, **kwargs):
        global models
        drops = tuple(drops)
        required_model = (file_name, primary_classified, drops)
        if required_model not in self.models:
            model = cm.run(file_name, primary_classified, drops)
            self.models[required_model] = (model, primary_classified)
            print("New model created: " + file_name)
        result = self.execute_for_server(self.models[required_model][0], self.models[required_model][1], **kwargs)
        return result

    def execute_for_server(self, model, primary_classified, **kwargs):
        result = pt.execute(model, primary_classified, **kwargs)
        return result