@echo off
echo Starting Bengaluru House Price Predictor...
echo ============================================

REM Change to the backend directory
cd /d "%~dp0backend"

REM Start the Flask server using main Anaconda Python
"S:\mldeeplearningai\python.exe" app.py

pause
