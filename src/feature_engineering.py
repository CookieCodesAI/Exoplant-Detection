import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def preprocess(csv):
    df = pd.read_csv(csv)
    columns_to_drop = [
    'kepid',                
    'kepoi_name',           
    'kepler_name',         
    'koi_pdisposition',     
    'koi_score',            
    'koi_tce_plnt_num',     
    'koi_tce_delivname',    
    'koi_time0bk',          
    'koi_time0bk_err1',
    'koi_time0bk_err2',
    'koi_period_err1',
    'koi_period_err2',
    'koi_impact',           
    'koi_impact_err1',
    'koi_impact_err2',
    'koi_duration_err1',
    'koi_duration_err2',
    'koi_depth_err1',
    'koi_depth_err2',
    'koi_prad_err1',
    'koi_prad_err2',
    'koi_teq_err1',
    'koi_teq_err2',
    'koi_insol_err1',
    'koi_insol_err2',
    'koi_steff_err1',
    'koi_steff_err2',
    'koi_slogg_err1',
    'koi_slogg_err2',
    'koi_srad_err1',
    'koi_srad_err2',
    'ra',
    'dec',
    'koi_kepmag'
    ]
    cleaned = df.drop(columns = columns_to_drop)
    cleaned = df.dropna(subset=['koi_disposition'])
    cleaned = df.fillna(df.mean(numeric_only=True))

    le = LabelEncoder()
    cleaned['output'] = le.fit_transform(cleaned['koi_disposition'])

    features = [
        'koi_period', 
        'koi_duration', 
        'koi_depth',
        'koi_prad',
        'koi_teq', 
        'koi_insol', 
        'koi_model_snr', 
        'koi_steff',
        'koi_slogg', 
        'koi_srad', 
        'koi_fpflag_nt', 
        'koi_fpflag_ss',
        'koi_fpflag_co', 
        'koi_fpflag_ec'
        ]
    
    X = cleaned[features] 
    y = cleaned['output']
    
    return X, y, le

