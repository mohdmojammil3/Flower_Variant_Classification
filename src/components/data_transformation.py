import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
import os

def preprocess_data(train_data, test_data):
    # Define columns to transform
    numeric_features = train_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_features = train_data.select_dtypes(include=['object']).columns.tolist()

    # Define preprocessing steps for numeric and categorical data
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median'))
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ordinal_encoder', OrdinalEncoder())
    ])

    # Combine transformers using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Fit and transform the data
    preprocessed_train_data = preprocessor.fit_transform(train_data)
    preprocessed_test_data = preprocessor.transform(test_data)

    # Get the column names for the processed data
    preprocessed_column_names = numeric_features + categorical_features

    # Convert the processed arrays back to DataFrames
    preprocessed_train_df = pd.DataFrame(preprocessed_train_data, columns=preprocessed_column_names)
    preprocessed_test_df = pd.DataFrame(preprocessed_test_data, columns=preprocessed_column_names)

    return preprocessed_train_df, preprocessed_test_df

def save_processed_data(train_data, test_data, train_file_path, test_file_path):
    train_data.to_csv(train_file_path, index=False)
    test_data.to_csv(test_file_path, index=False)

if __name__ == "__main__":
    train_data = pd.read_csv(os.path.join("data", "traindata", "train.csv"))
    test_data = pd.read_csv(os.path.join("data", "testdata", "test.csv"))
    preprocessed_train_data, preprocessed_test_data = preprocess_data(train_data, test_data)
    save_processed_data(preprocessed_train_data, preprocessed_test_data, os.path.join("data", "processed", "processed_train.csv"), os.path.join("data", "processed", "processed_test.csv"))
