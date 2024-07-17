import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model(train_data):
    X_train = train_data.drop("species", axis=1)
    y_train = train_data["species"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model

def save_model(model, model_file_path):
    joblib.dump(model, model_file_path)

if __name__ == "__main__":
    train_data = pd.read_csv(os.path.join("data", "processed", "processed_train.csv"))
    trained_model = train_model(train_data)
    save_model(trained_model, os.path.join("models", "model.pkl"))
