# Android Build Script for SlugRace (Windows PowerShell)
# Make sure you have buildozer installed: pip install buildozer

Write-Host "Building SlugRace for Android..." -ForegroundColor Green

# Check if buildozer is installed
try {
    buildozer --version | Out-Null
} catch {
    Write-Host "ERROR: buildozer is not installed. Install it with:" -ForegroundColor Red
    Write-Host "pip install buildozer" -ForegroundColor Yellow
    exit 1
}

# Check platform
if (-not ($env:OS -match "Windows")) {
    Write-Host "WARNING: This script is for Windows. Use build_android.sh on Linux/Mac" -ForegroundColor Yellow
}

# Recommend WSL for Windows users
Write-Host "NOTE: For best results on Windows, consider using WSL (Windows Subsystem for Linux)" -ForegroundColor Cyan

# Clean previous builds
Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
buildozer android clean

# Build debug APK
Write-Host "Building debug APK..." -ForegroundColor Yellow
buildozer android debug

# Check if build was successful
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Build successful!" -ForegroundColor Green
    Write-Host "APK location: bin\slugrace-1.0-debug.apk" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "To install on device: adb install bin\slugrace-1.0-debug.apk" -ForegroundColor Yellow
    Write-Host "Or copy the APK to your Android device and install manually" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "❌ Build failed!" -ForegroundColor Red
    Write-Host "Check the error messages above for troubleshooting" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Common solutions:" -ForegroundColor Cyan
    Write-Host "1. Install required dependencies (Java JDK, Android SDK)" -ForegroundColor White
    Write-Host "2. Use WSL for better compatibility" -ForegroundColor White
    Write-Host "3. Check buildozer.spec configuration" -ForegroundColor White
}