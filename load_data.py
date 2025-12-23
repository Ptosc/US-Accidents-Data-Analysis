import pandas as pd

def load_data():
    columns = []
    path = ''
    df = pd.read_csv(path, usecols=columns)

    return df