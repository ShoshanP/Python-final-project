import pandas as pd


class FileOperation:

    def __init__(self, data):
        self.data = data

    def read_excel(self, file_path: str):
        self.data = pd.read_csv(file_path)

    def save_to_excel(self, data, file_name: str):
        data.to_csv(file_name)
