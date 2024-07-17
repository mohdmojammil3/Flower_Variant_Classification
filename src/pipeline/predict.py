import numpy as np
import pandas as pd
import joblib
import os

def load_model(model_file_path):
    return joblib.load(model_file_path)

def make_prediction(model, input_data):
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    input_df = pd.DataFrame(input_data, columns=column_names)
    return model.predict(input_df)

if __name__ == "__main__":
    model = load_model(os.path.join("models", "model.pkl"))
    # Example input for testing purposes
    input_data = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = make_prediction(model, input_data)
    print(prediction)
