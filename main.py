from src.feature_engineering import preprocess
from src.model import make_pipeline, make_model
from src.evaluate import evaluate
from src.train import predict_exoplanet

def main():

    X, y, _ = preprocess('data/Kepler_IDs.csv')
    pipeline = make_pipeline()
    model, X_train, X_test,  y_train, y_test = make_model(pipeline, X, y)
    evaluate(model, X_test, y_test)
    
    features = {
    'koi_period': 0.75,         
    'koi_duration': 1.2,
    'koi_depth': 50.0,          
    'koi_prad': 0.3,       
    'koi_teq': 3000.0,         
    'koi_insol': 5000.0,   
    'koi_model_snr': 3.1,     
    'koi_steff': 6500.0,         
    'koi_slogg': 4.9,            
    'koi_srad': 1.8               
}   
    prediction = predict_exoplanet(features)
    if prediction == 0:
        result = "Confirmed"
    else:
        result = "False Positive"
    print("This stellar object is most likely a: ", result)

if __name__ == '__main__':
    main()