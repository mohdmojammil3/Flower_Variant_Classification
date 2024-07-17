# Flower Variant Classification
This project is aimed at predicting flower variants based on several features such as petal length, petal width, sepal length, and sepal width. The model utilized for prediction is RandomForestClassifier, which is known for its robustness and accuracy.

# Features Used:

* Petal Length: Length of the petal in centimeters.
* Petal Width: Width of the petal in centimeters.
* Sepal Length: Length of the sepal in centimeters.
* Sepal Width: Width of the sepal in centimeters.

# Dataset:
The dataset consists of multiple flower samples, each labeled with its variant.
Data is split into training and testing sets to evaluate model performance.

# Preprocessing:
* Handling missing values.
* Encoding categorical variables.
* Normalizing/standardizing numerical features.

* Model:
RandomForestClassifier: A versatile and widely-used ensemble learning method that constructs multiple decision trees and merges them to get a more accurate and stable prediction.


# Table of Contents

* Installation
* Project Structure
* Usage
* Model Training
* Prediction
* References
* License

# Installation


* Clone the repository:

* Copy code
git clone https://github.com/mohdmojammil3/Flower-Variant-Prediction.git
cd Flower-Variant-Prediction

# Create a virtual environment and activate it:

* Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages:


* Copy code:
pip install -r requirements.txt
Project Structure

# The project follows the following structure:


Flower-Variant-Prediction/
│
├── .ebextensions/
│   └── python.config        # Configuration file for Elastic Beanstalk deployment
│
├── data/
│   ├── train_data.csv       # Raw training data
│   └── test_data.csv        # Raw test data
│
├── models/
│   ├── preprocessor.pkl     # Serialized data preprocessor
│   └── model.pkl            # Serialized best performing model (RandomForestClassifier)
│
├── notebooks/
│   ├── EDA.ipynb            # Exploratory Data Analysis notebook
│   ├── Model.ipynb          # Model training and evaluation notebook
│   └── research.ipynb       # Research and experimentation notebook
│
├── src/
│   ├── data_preprocessing.py# Data preprocessing scripts
│   ├── model_trainer.py     # Model training script
│   └── data_ingestion.py    # Data ingestion script
│
├── static/
│   └── image.jpg            # Static image
│
├── templates/
│   └── index.html           # HTML template for the web interface
│
├── .gitignore               # Git ignore file
├── app.py                   # Flask application script
├── requirements.txt         # List of Python dependencies
└── README.md                # This file

# Usage

* To run the application:

Copy code
python app.py

Open your web browser and go to http://127.0.0.1:5000.

# Model Training

The model is trained using the RandomForestClassifier algorithm. The training process includes the following steps:

* Data Ingestion: Load and preprocess the training data.
* Data Preprocessing: Handle missing values, encode categorical features, and scale numerical features.
* Model Training: Train the RandomForestClassifier model using the preprocessed training data.
Prediction


# To make predictions using the trained model:

* Load the preprocessor and model from their respective .pkl files.
* Preprocess the input data using the preprocessor.
* Use the model to predict flower variants based on the preprocessed data.


# References

* Pandas Documentation
* Scikit-Learn Documentation
* Flask Documentation
* Elastic Beanstalk Documentation

# License
* This project is licensed under the MIT License - see the LICENSE file for details.