#!/usr/bin/env python3
"""
Script to check which packages are available for the ML project
"""

def check_package(package_name, import_name=None):
    if import_name is None:
        import_name = package_name
    
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'Unknown version')
        print(f"✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"❌ {package_name}: Not installed")
        return False

print("Checking required packages for Bengaluru House Price Prediction:")
print("=" * 60)

# Check required packages
packages = [
    ('NumPy', 'numpy'),
    ('Pandas', 'pandas'),
    ('Scikit-learn', 'sklearn'),
    ('Flask', 'flask'),
    ('Flask-CORS', 'flask_cors'),
    ('Pickle', 'pickle')
]

missing_packages = []
for package_name, import_name in packages:
    if not check_package(package_name, import_name):
        missing_packages.append(package_name)

print("\n" + "=" * 60)
if missing_packages:
    print(f"Missing packages: {', '.join(missing_packages)}")
    print("\nTo install missing packages, run:")
    print("pip install flask flask-cors")
else:
    print("✅ All required packages are available!")
    
print("\nPackages needed for this project:")
print("- Flask (for web API)")
print("- Flask-CORS (for handling cross-origin requests)")
print("- NumPy (for numerical operations)")
print("- Pandas (for data handling)")
print("- Scikit-learn (for the ML model)")
print("- Pickle (built-in Python module for model serialization)")
