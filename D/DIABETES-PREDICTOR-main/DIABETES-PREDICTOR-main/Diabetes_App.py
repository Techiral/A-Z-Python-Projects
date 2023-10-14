import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

#Creating the flask app
app = Flask(__name__)

model = joblib.load("Diabetes_Model1.pkl")

@app.route('/')
def home():
    return render_template('Diabetes_App.html')

@app.route('/predict', methods=['POST'])
def predict():
  
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if (prediction[0] > 0.5):
        return render_template('Diabetes_App.html', prediction_text='RESULTS: You are in high risk of diabetes')
    

    else:
        return render_template('Diabetes_App.html', prediction_text= 'RESULTS: You are in low risk of diabetes')
    

if __name__ == "__main__":
    app.run(debug=True)