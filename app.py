from flask import Flask, request, render_template
from src.train import predict_exoplanet
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        features = {
            'koi_period': float(request.form['koi_period']), 
            'koi_duration': float(request.form['koi_duration']), 
            'koi_depth': float(request.form['koi_depth']),
            'koi_prad': float(request.form['koi_prad']),
            'koi_teq': float(request.form['koi_teq']), 
            'koi_insol': float(request.form['koi_insol']), 
            'koi_model_snr': float(request.form['koi_model_snr']), 
            'koi_steff': float(request.form['koi_steff']),
            'koi_slogg': float(request.form['koi_slogg']), 
            'koi_srad':float(request.form['koi_srad'])
        }
        prediction = predict_exoplanet(features)
        if prediction == 0:
            final = "Confirmed"
        else:
            final = "False Positive"
        result = f"This stellar object is most likely: {final}"
    return render_template("index.html", result = result )
if __name__ == "__main__":
    app.run(debug=True)