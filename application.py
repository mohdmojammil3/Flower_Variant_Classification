from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib
import os

application = Flask(__name__)

app = application

model = joblib.load(os.path.join("models", "model.pkl"))

# Dictionary to map numeric predictions to species names
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        if not (0 < sepal_length < 10) or not (0 < sepal_width < 10) or not (0 < petal_length < 10) or not (0 < petal_width < 10):
            return render_template('index.html', prediction="Invalid input")

        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        features_df = pd.DataFrame(features, columns=column_names)
        prediction = model.predict(features_df)
        species = species_mapping[prediction[0]]

        # Debugging print statement
        print(f"Predicted species: {species}")

        return render_template('index.html', prediction=species)
    except ValueError:
        return render_template('index.html', prediction="Invalid input")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
