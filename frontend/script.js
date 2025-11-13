// API base URL - automatically detects current domain
const API_BASE_URL = window.location.origin;

// DOM elements
const locationSelect = document.getElementById('location');
const priceForm = document.getElementById('priceForm');
const resultSection = document.getElementById('resultSection');
const priceResult = document.getElementById('priceResult');
const propertyDetails = document.getElementById('propertyDetails');
const loading = document.getElementById('loading');

// Load locations when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadLocations();
    setupFormSubmission();
});

// Load all available locations from the API
async function loadLocations() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/get_location_names`);
        const data = await response.json();
        
        if (data.locations) {
            data.locations.forEach(location => {
                const option = document.createElement('option');
                option.value = location;
                option.textContent = formatLocationName(location);
                locationSelect.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading locations:', error);
        showError('Failed to load locations. Please check if the backend server is running.');
    }
}

// Format location names for better display
function formatLocationName(location) {
    return location.split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

// Setup form submission
function setupFormSubmission() {
    priceForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = {
            location: document.getElementById('location').value,
            total_sqft: document.getElementById('sqft').value,
            bhk: document.getElementById('bhk').value,
            bath: document.getElementById('bath').value
        };
        
        // Validate form data
        if (!validateForm(formData)) {
            return;
        }
        
        // Show loading
        showLoading(true);
        hideResult();
        
        try {
            // Make API call
            const response = await fetch(`${API_BASE_URL}/api/predict_home_price`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (response.ok) {
                // Show result
                showResult(data);
            } else {
                // Show error
                showError(data.error || 'An error occurred while predicting the price');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Failed to connect to the server. Please check if the backend is running.');
        } finally {
            showLoading(false);
        }
    });
}

// Validate form data
function validateForm(data) {
    if (!data.location) {
        showError('Please select a location');
        return false;
    }
    
    if (!data.total_sqft || data.total_sqft < 100) {
        showError('Please enter a valid square feet (minimum 100)');
        return false;
    }
    
    if (!data.bhk || data.bhk < 1 || data.bhk > 12) {
        showError('Please select number of bedrooms (1-12 BHK)');
        return false;
    }
    
    if (!data.bath || data.bath < 1 || data.bath > 12) {
        showError('Please select number of bathrooms (1-12)');
        return false;
    }
    
    return true;
}

// Show prediction result
function showResult(data) {
    const price = data.estimated_price;
    const location = formatLocationName(data.location);
    const predictionType = data.prediction_type;
    const message = data.message;
    
    // Handle different prediction types
    if (predictionType === 'no_houses') {
        priceResult.innerHTML = `
            <div class="price-value no-houses">
                <i class="fas fa-exclamation-triangle"></i>
                <div class="no-houses-message">
                    <h4>No Houses Found</h4>
                    <p>${message}</p>
                </div>
            </div>
        `;
    } else if (predictionType === 'few_houses') {
        priceResult.innerHTML = `
            <div class="price-value few-houses">
                <i class="fas fa-info-circle"></i>
                <div class="few-houses-info">
                    <div class="price-amount">₹${price} Lakhs</div>
                    <p class="warning-message">${message}</p>
                </div>
            </div>
        `;
    } else {
        priceResult.innerHTML = `
            <div class="price-value">
                <i class="fas fa-rupee-sign"></i>
                ${price} Lakhs
            </div>
            <div class="prediction-confidence">
                <small>${message}</small>
            </div>
        `;
    }
    
    // Show property details only if houses are found
    if (predictionType !== 'no_houses') {
        propertyDetails.innerHTML = `
            <div class="details-grid">
                <div class="detail-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <span>Location: ${location}</span>
                </div>
                <div class="detail-item">
                    <i class="fas fa-expand-arrows-alt"></i>
                    <span>Area: ${data.total_sqft} sq ft</span>
                </div>
                <div class="detail-item">
                    <i class="fas fa-bed"></i>
                    <span>Bedrooms: ${data.bhk} BHK</span>
                </div>
                <div class="detail-item">
                    <i class="fas fa-bath"></i>
                    <span>Bathrooms: ${data.bath}</span>
                </div>
            </div>
            ${price > 0 ? `<div class="price-per-sqft">
                <small>Price per sq ft: ₹${Math.round((price * 100000) / data.total_sqft).toLocaleString()}</small>
            </div>` : ''}
        `;
    } else {
        propertyDetails.innerHTML = `
            <div class="no-houses-suggestions">
                <h4>Try these alternatives:</h4>
                <ul>
                    <li>Select a different location</li>
                    <li>Adjust the square footage</li>
                    <li>Try different BHK/bathroom combinations</li>
                    <li>Consider nearby areas</li>
                </ul>
            </div>
        `;
    }
    
    resultSection.style.display = 'block';
    resultSection.scrollIntoView({ behavior: 'smooth' });
}

// Show error message
function showError(message) {
    priceResult.innerHTML = `
        <div class="error-message">
            <i class="fas fa-exclamation-triangle"></i>
            ${message}
        </div>
    `;
    propertyDetails.innerHTML = '';
    resultSection.style.display = 'block';
}

// Show/hide loading
function showLoading(show) {
    loading.style.display = show ? 'block' : 'none';
}

// Hide result section
function hideResult() {
    resultSection.style.display = 'none';
}

// Format number with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
