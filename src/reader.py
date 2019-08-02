import pandas as pd
import os


class Reader:
    def __init__(self, filename, location):
        self.file = filename
        self.location = location
        self.path = os.path.basename(os.getcwd())


    def csv_to_df(self):
        os.chdir('../' + self.location)
        data = pd.read_csv(self.file)
        os.chdir('../' + self.path)
        return data


