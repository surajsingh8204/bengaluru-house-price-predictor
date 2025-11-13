# Quick Start - Deploy to Internet

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Bengaluru House Price Predictor" -ForegroundColor Yellow
Write-Host "Quick Deployment Setup" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
Write-Host "Checking if Git is installed..." -ForegroundColor Green
$gitInstalled = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitInstalled) {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Please download and install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit
}
Write-Host "✓ Git is installed" -ForegroundColor Green
Write-Host ""

# Initialize git if not already done
if (-not (Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Green
    git init
    git add .
    git commit -m "Initial commit - Bengaluru House Price Predictor"
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "✓ Git repository already exists" -ForegroundColor Green
}
Write-Host ""

# Instructions for GitHub
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Create a NEW repository on GitHub:" -ForegroundColor White
Write-Host "   - Go to: https://github.com/new" -ForegroundColor Cyan
Write-Host "   - Repository name: bengaluru-house-price-predictor" -ForegroundColor Cyan
Write-Host "   - Make it PUBLIC" -ForegroundColor Cyan
Write-Host "   - DON'T initialize with README" -ForegroundColor Cyan
Write-Host ""

Write-Host "2. After creating the repository, run these commands:" -ForegroundColor White
Write-Host "   (Replace YOUR_USERNAME with your GitHub username)" -ForegroundColor Yellow
Write-Host ""
Write-Host '   git remote add origin https://github.com/YOUR_USERNAME/bengaluru-house-price-predictor.git' -ForegroundColor Cyan
Write-Host '   git branch -M main' -ForegroundColor Cyan
Write-Host '   git push -u origin main' -ForegroundColor Cyan
Write-Host ""

Write-Host "3. Deploy on Render (FREE):" -ForegroundColor White
Write-Host "   - Go to: https://render.com" -ForegroundColor Cyan
Write-Host "   - Sign up with GitHub" -ForegroundColor Cyan
Write-Host "   - Click 'New +' -> 'Web Service'" -ForegroundColor Cyan
Write-Host "   - Connect your repository" -ForegroundColor Cyan
Write-Host "   - Build Command: pip install -r requirements.txt" -ForegroundColor Cyan
Write-Host "   - Start Command: gunicorn backend.app:app" -ForegroundColor Cyan
Write-Host "   - Click 'Create Web Service'" -ForegroundColor Cyan
Write-Host ""

Write-Host "4. Wait 5-10 minutes and your app will be LIVE! 🚀" -ForegroundColor Green
Write-Host ""
Write-Host "For detailed instructions, read: DEPLOYMENT_GUIDE.md" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
