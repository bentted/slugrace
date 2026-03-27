#!/bin/bash

# Android Build Script for SlugRace
# Make sure you have buildozer installed: pip install buildozer

echo "Building SlugRace for Android..."

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "ERROR: buildozer is not installed. Install it with:"
    echo "pip install buildozer"
    exit 1
fi

# Check if we're on Linux/WSL
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "WARNING: Android builds are recommended on Linux or WSL"
    echo "You may encounter issues building on other platforms"
fi

# Clean previous builds
echo "Cleaning previous builds..."
buildozer android clean

# Build debug APK
echo "Building debug APK..."
buildozer android debug

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful!"
    echo "APK location: bin/slugrace-1.0-debug.apk"
    echo ""
    echo "To install on device: adb install bin/slugrace-1.0-debug.apk"
    echo "Or copy the APK to your Android device and install manually"
else
    echo ""
    echo "❌ Build failed!"
    echo "Check the error messages above for troubleshooting"
fi