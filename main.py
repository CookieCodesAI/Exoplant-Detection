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
        'koi_period': 12.34,      
        'koi_duration': 3.2,      
        'koi_depth': 500.0,         
        'koi_prad': 2.5,           
        'koi_teq': 800,            
        'koi_insol': 100.0,         
        'koi_model_snr': 50.0,      
        'koi_steff': 5778,         
        'koi_slogg': 4.4,           
        'koi_srad': .9 
    }
    
    prediction = predict_exoplanet(features)

    print("This stellar object is: ", str(prediction))

if __name__ == '__main__':
    main()