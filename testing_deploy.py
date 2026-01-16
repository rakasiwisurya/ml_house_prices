from flask import Flask, request, jsonify
import joblib
 
# Initialize the Flask application
app = Flask(__name__)
 
# Load the saved model
joblib_model = joblib.load('models/gbr_model.joblib') # Make sure the file path matches your storage.
 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']  # Retrieving data from JSON requests
    prediction = joblib_model.predict(data)  # Make predictions (must be in 2D array form)
    return jsonify({'prediction': prediction.tolist()})
 
if __name__ == '__main__':
    app.run(debug=True)