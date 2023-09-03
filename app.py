# heart_disease_predictor/app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Load your trained machine learning model
model = joblib.load('./model.pkl')

@app.route('/predict', methods=['POST'])
@cross_origin(origin='http://localhost:3000', allow_headers=['Content-Type'])
def predict():
    data = request.get_json()  # Get input data from the request
    print(data)
    # Convert the data to a Pandas DataFrame
    input_df = pd.DataFrame(data['features'], columns=[
        "Age", "Gender", "family_history", "benefits", "care_options", "anonymity", "leave", "work_interfere"
    ])

    # Process the features and make predictions using the model
    prediction = model.predict(input_df)

    # Return the prediction as JSON response
    response = {'prediction': prediction.tolist()}
    output = response["prediction"][0]
    return jsonify(response) 

if __name__ == '__main__':
    app.run(debug=True)