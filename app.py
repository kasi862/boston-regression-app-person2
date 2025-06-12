from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f'feature{i}']) for i in range(1, 14)]
        prediction = model.predict([features])
        prediction_value = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Predicted Price: ${prediction_value}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: Please enter valid numbers. ({e})')

# Required for Render deployment
if __name__ != '__main__':
    # Gunicorn needs this to expose the app object
    gunicorn_app = app

if __name__ == "__main__":
    app.run(debug=True)

