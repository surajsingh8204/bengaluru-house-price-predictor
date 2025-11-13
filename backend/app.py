from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import json
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Add cache control headers to prevent browser caching during development
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(project_root, 'mlmodel', 'bengaluru_home_prices_model.pickle')
columns_path = os.path.join(project_root, 'mlmodel', 'columns.json')

# Load the model and columns data
with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(columns_path, 'r') as f:
    data_columns = json.load(f)['data_columns']

def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Find the index of the location in data_columns
        loc_index = -1
        if location.lower() in [col.lower() for col in data_columns]:
            # Find the exact match (case insensitive)
            for i, col in enumerate(data_columns):
                if col.lower() == location.lower():
                    loc_index = i
                    break
        
        # Create feature array
        x = np.zeros(len(data_columns))
        x[0] = sqft    # total_sqft
        x[1] = bath    # bath
        x[2] = bhk     # bhk
        
        if loc_index >= 0:
            x[loc_index] = 1
        
        # Make prediction
        predicted_price = model.predict([x])[0]
        
        # Handle negative or very low prices
        if predicted_price <= 0:
            return {
                'type': 'no_houses',
                'message': 'No houses found with this combination of features in this location. Try different parameters.',
                'price': 0
            }
        elif predicted_price < 5:  # Less than 5 lakhs
            return {
                'type': 'few_houses',
                'message': 'Very few houses available with these specifications. Price might be uncertain.',
                'price': round(predicted_price, 2)
            }
        else:
            return {
                'type': 'normal',
                'message': 'Price prediction based on market data',
                'price': round(predicted_price, 2)
            }
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return None

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    """Return all available locations"""
    locations = [col for col in data_columns if col not in ['total_sqft', 'bath', 'bhk']]
    return jsonify({
        'locations': locations
    })

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    """Predict house price based on input parameters"""
    try:
        # Get data from request
        data = request.get_json()
        
        location = data.get('location', '').strip()
        sqft = float(data.get('total_sqft', 0))
        bhk = int(data.get('bhk', 0))
        bath = int(data.get('bath', 0))
        
        # Validate inputs
        if not location:
            return jsonify({
                'error': 'Please provide a valid location'
            }), 400
        
        if sqft < 100 or sqft > 50000:
            return jsonify({
                'error': 'Square feet must be between 100 and 50,000'
            }), 400
            
        if bhk < 1 or bhk > 12:
            return jsonify({
                'error': 'BHK must be between 1 and 12'
            }), 400
            
        if bath < 1 or bath > 12:
            return jsonify({
                'error': 'Bathrooms must be between 1 and 12'
            }), 400
        
        # Get prediction
        result = get_estimated_price(location, sqft, bhk, bath)
        
        if result is None:
            return jsonify({
                'error': 'Error occurred during prediction'
            }), 500
        
        return jsonify({
            'estimated_price': result['price'],
            'prediction_type': result['type'],
            'message': result['message'],
            'location': location,
            'total_sqft': sqft,
            'bhk': bhk,
            'bath': bath
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Bengaluru House Price Prediction API is running'
    })

@app.route('/', methods=['GET'])
def home():
    """Serve the main HTML page"""
    frontend_path = os.path.join(project_root, 'frontend')
    return send_from_directory(frontend_path, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, etc.)"""
    frontend_path = os.path.join(project_root, 'frontend')
    return send_from_directory(frontend_path, filename)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """Serve assets files (images, etc.)"""
    assets_path = os.path.join(project_root, 'assets')
    return send_from_directory(assets_path, filename)

@app.route('/api/', methods=['GET'])
def api_home():
    """Root API endpoint with information"""
    return jsonify({
        'message': 'Bengaluru House Price Prediction API',
        'version': '1.0',
        'endpoints': {
            'predict': '/api/predict_home_price (POST)',
            'locations': '/api/get_location_names (GET)',
            'health': '/api/health (GET)'
        }
    })

if __name__ == '__main__':
    print("Starting Flask server for Bengaluru House Price Prediction...")
    print("Model and data loaded successfully!")
    app.run(debug=True, host='0.0.0.0', port=5000)
