import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import joblib 

def make_pipeline():
    pipeline = Pipeline([
        ('imputer', SimpleImputer()),
        ('tree', DecisionTreeClassifier())
        ])
    return pipeline

def make_model(pipeline, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, "models/decision_tree.pkl")
    return pipeline, X_train, X_test,  y_train, y_test

