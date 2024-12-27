import pandas as pd

def read_data(data_path):
    df = pd.read_csv(data_path, )
    content = df.iloc[:, 0].to_list()
    label = df.iloc[:, 1].to_list()
    return content, label