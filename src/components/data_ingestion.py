import pandas as pd
from sklearn.model_selection import train_test_split
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def split_data(data, test_size=0.2):
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
    return train_data, test_data

def save_data(train_data, test_data, train_file_path, test_file_path):
    train_data.to_csv(train_file_path, index=False)
    test_data.to_csv(test_file_path, index=False)

if __name__ == "__main__":
    raw_data = load_data(os.path.join("data", "raw", "iris.csv"))
    train_data, test_data = split_data(raw_data)
    save_data(train_data, test_data, os.path.join("data", "traindata", "train.csv"), os.path.join("data", "testdata", "test.csv"))
