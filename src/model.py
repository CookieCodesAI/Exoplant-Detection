import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer

def make_pipeline():
    pipeline = Pipeline(tree = DecisionTreeClassifier())
    return pipeline

