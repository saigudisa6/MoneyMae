from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for your Flask app to allow requests from the React frontend's origin

CORS(app, resources={r"/submit": {"origins": "http://localhost:5173/input"}})

# Define a route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json  # Get the JSON data from the request

    # Process the form data
    name = data.get('id')
    email = data.get('carPay')

    # Perform any necessary actions with the data
    # For example, save it to a database

    return jsonify({"message": "Form data received successfully"})

if __name__ == '__main__':
    app.run(debug=True)