import pandas as pd
import numpy as np
import joblib 

def predict_exoplanet(features):

    order = [
        'koi_period', 
        'koi_duration', 
        'koi_depth',
        'koi_prad',
        'koi_teq', 
        'koi_insol', 
        'koi_model_snr', 
        'koi_steff',
        'koi_slogg', 
        'koi_srad'
        ]
    user_input = np.array([[features[feature] for feature in order]])
    model = joblib.load('models/decision_tree.pkl')
    prediction = model.predict(user_input)
    return prediction