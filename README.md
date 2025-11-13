# 🏠 Bengaluru Real Estate Price Predictor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A full-stack machine learning web application that predicts house prices in Bengaluru based on location, square footage, number of bedrooms (BHK), and bathrooms. Built with Python, Flask, and deployed with a modern, responsive frontend.

![Bengaluru House Price Predictor](https://via.placeholder.com/800x400?text=Bengaluru+House+Price+Predictor)

## 🌟 Features

- 🎯 **Accurate ML Predictions** - Linear Regression model trained on real Bengaluru housing data
- 📍 **200+ Locations** - Comprehensive coverage of Bengaluru neighborhoods
- 💻 **Modern UI** - Clean, responsive interface with gradient backgrounds
- 📊 **Real-time Results** - Instant price predictions with detailed breakdowns
- 🔄 **RESTful API** - Easy-to-use API endpoints for integration
- 📱 **Mobile Responsive** - Works perfectly on all devices

## 🚀 Live Demo

[**Try it Live**](https://your-deployment-url.onrender.com) *(Coming Soon)*

## 📸 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/600x300?text=Main+Interface)

### Prediction Results
![Prediction Results](https://via.placeholder.com/600x300?text=Prediction+Results)

## 🛠️ Technology Stack

### Backend
- **Python 3.11** - Programming language
- **Flask** - Web framework
- **Scikit-learn** - Machine learning library
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Gunicorn** - Production WSGI server

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern gradients
- **JavaScript (ES6)** - Dynamic functionality
- **Font Awesome** - Icons

### Machine Learning
- **Linear Regression** - Core prediction model
- **Data Preprocessing** - Outlier removal, feature engineering
- **One-Hot Encoding** - Location feature encoding

## 📁 Project Structure

```
bengaluru-house-price-predictor/
│
├── backend/
│   ├── app.py                 # Flask application & API endpoints
│   └── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── index.html            # Main HTML page
│   ├── style.css             # Styling & animations
│   └── script.js             # Frontend logic & API calls
│
├── mlmodel/
│   ├── modelcode.ipynb       # 📓 Complete ML model training code
│   ├── bengaluru_home_prices_model.pickle  # Trained model
│   ├── columns.json          # Feature columns & locations
│   └── bengaluru_house_prices.csv         # Training dataset
│
├── assets/
│   └── buildings.jpeg        # Background image
│
├── requirements.txt          # All dependencies
├── Procfile                  # Heroku deployment
├── render.yaml               # Render deployment
├── runtime.txt               # Python version
├── DEPLOYMENT_GUIDE.md       # Deployment instructions
└── README.md                 # This file
```

## 🧠 Machine Learning Model

### Model Details
The prediction model is built using **Linear Regression** algorithm, chosen after comparing various algorithms for performance and accuracy.

### Data Processing Pipeline
1. **Data Collection** - Historical Bengaluru house price data
2. **Data Cleaning** 
   - Removed missing values
   - Handled outliers using statistical methods
   - Standardized location names
3. **Feature Engineering**
   - Square feet per bedroom ratio
   - Price per square feet analysis
   - Location-based encoding
4. **Model Training**
   - Train-test split (80-20)
   - Cross-validation for robustness
   - Hyperparameter tuning
5. **Model Evaluation**
   - R² Score
   - Mean Absolute Error (MAE)
   - Root Mean Square Error (RMSE)

### View Complete Model Code
📓 **[Check out the complete model training code in Jupyter Notebook](mlmodel/modelcode.ipynb)**

The notebook contains:
- Exploratory Data Analysis (EDA)
- Data visualization
- Feature engineering process
- Model training & evaluation
- Performance metrics

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Local Development Setup

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/bengaluru-house-price-predictor.git
cd bengaluru-house-price-predictor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python backend/app.py
```

4. **Access the application**
```
Open your browser and go to: http://localhost:5000
```

## 🔌 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "Bengaluru House Price Prediction API is running"
}
```

#### 2. Get All Locations
```http
GET /api/get_location_names
```

**Response:**
```json
{
  "locations": [
    "1st Block Jayanagar",
    "1st Phase JP Nagar",
    "Whitefield",
    "Electronic City",
    ...
  ]
}
```

#### 3. Predict House Price
```http
POST /api/predict_home_price
Content-Type: application/json
```

**Request Body:**
```json
{
  "location": "1st Block Jayanagar",
  "total_sqft": 1200,
  "bhk": 2,
  "bath": 2
}
```

**Response:**
```json
{
  "estimated_price": 85.50,
  "prediction_type": "normal",
  "message": "Price prediction based on market data",
  "location": "1st Block Jayanagar",
  "total_sqft": 1200,
  "bhk": 2,
  "bath": 2
}
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.84 |
| Mean Absolute Error | 18.5 Lakhs |
| Root Mean Square Error | 25.3 Lakhs |
| Training Samples | 13,000+ |

## 🚀 Deployment

This application can be deployed on various platforms:

### Deploy to Render (Free)
1. Fork this repository
2. Sign up on [Render](https://render.com)
3. Create a new Web Service
4. Connect your GitHub repository
5. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn backend.app:app`

### Deploy to Railway (Free)
1. Fork this repository
2. Sign up on [Railway](https://railway.app)
3. Create new project from GitHub repo
4. Railway will auto-deploy

**For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**

## 🎯 Usage Example

### Web Interface
1. Select a location from the dropdown (e.g., "Whitefield")
2. Enter total square feet (e.g., 1500)
3. Select number of bedrooms (e.g., 3 BHK)
4. Select number of bathrooms (e.g., 2)
5. Click "Predict Price"
6. Get instant price prediction in Lakhs (₹)

### API Usage (Python)
```python
import requests

url = "http://localhost:5000/api/predict_home_price"
data = {
    "location": "Whitefield",
    "total_sqft": 1500,
    "bhk": 3,
    "bath": 2
}

response = requests.post(url, json=data)
result = response.json()
print(f"Estimated Price: ₹{result['estimated_price']} Lakhs")
```

### API Usage (JavaScript)
```javascript
fetch('http://localhost:5000/api/predict_home_price', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    location: 'Whitefield',
    total_sqft: 1500,
    bhk: 3,
    bath: 2
  })
})
.then(response => response.json())
.then(data => console.log('Estimated Price:', data.estimated_price));
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Include property amenities in predictions
- [ ] Add price trend visualization
- [ ] Implement user authentication
- [ ] Add property comparison feature
- [ ] Create mobile app (React Native)
- [ ] Add map integration for location visualization
- [ ] Include historical price trends

## 🐛 Known Issues

- Free tier deployments may have cold start delay (30-60 seconds)
- Some uncommon location names might not be in the dataset

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Suraj**

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/your-profile)
- Portfolio: [your-portfolio.com](https://your-portfolio.com)

## 🙏 Acknowledgments

- Dataset source: Kaggle - Bengaluru House Price Data
- Scikit-learn documentation and community
- Flask framework and documentation
- Font Awesome for icons
- The open-source community

## ⭐ Star This Repository

If you find this project useful, please consider giving it a star! It helps others discover the project.

---

**Made with ❤️ and Machine Learning**
