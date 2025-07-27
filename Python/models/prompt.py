class Prompt:
    def __init__(self, _data_file_name : str, _classified_by : str, _ignore_cols : list, _parameters : dict = {}):
        self.data_file_name = _data_file_name
        self.classified_by = _classified_by
        self.ignore_cols = _ignore_cols
        self.parameters = _parameters


