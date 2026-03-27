#!/bin/bash

# iOS Build Script for SlugRace
# This script requires macOS and Xcode

echo "Building SlugRace for iOS..."

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "ERROR: iOS builds require macOS with Xcode installed"
    exit 1
fi

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "ERROR: buildozer is not installed. Install it with:"
    echo "pip install buildozer"
    exit 1
fi

# Check if Xcode is installed
if ! command -v xcodebuild &> /dev/null; then
    echo "ERROR: Xcode is not installed. Install it from the App Store"
    exit 1
fi

# Check for iOS development setup
echo "Checking iOS development requirements..."

# Install kivy-ios if not present
if ! python -c "import kivy_ios" 2>/dev/null; then
    echo "Installing kivy-ios..."
    pip install kivy-ios
fi

# Clean previous builds
echo "Cleaning previous builds..."
buildozer ios clean

# Build iOS project
echo "Building iOS project..."
buildozer ios debug

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ iOS project generated successfully!"
    echo "Project location: platforms/ios/"
    echo ""
    echo "Next steps:"
    echo "1. Open the Xcode project in platforms/ios/"
    echo "2. Configure signing & capabilities in Xcode"
    echo "3. Connect your iOS device"
    echo "4. Build and run from Xcode"
    echo ""
    echo "Note: You need an Apple Developer account to run on physical devices"
else
    echo ""
    echo "❌ Build failed!"
    echo "Check the error messages above for troubleshooting"
    echo ""
    echo "Common solutions:"
    echo "1. Ensure Xcode command line tools are installed"
    echo "2. Update buildozer and kivy-ios to latest versions"
    echo "3. Check that all iOS dependencies are properly configured"
fi