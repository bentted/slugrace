#!/bin/bash

# Mobile Development Setup Script for SlugRace
# This script sets up the development environment for building mobile apps

echo "🐌 SlugRace Mobile Development Setup"
echo "===================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python installation
if ! command_exists python && ! command_exists python3; then
    echo "❌ Python is not installed. Please install Python 3.8 or later"
    exit 1
else
    echo "✅ Python found"
fi

# Use python3 if available, otherwise python
if command_exists python3; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
else
    PYTHON_CMD=python
    PIP_CMD=pip
fi

echo "Using Python: $($PYTHON_CMD --version)"

# Install core requirements
echo ""
echo "📦 Installing core requirements..."
$PIP_CMD install -r requirements.txt

# Platform-specific setup
case "$OSTYPE" in
    # Linux setup
    linux-gnu*)
        echo ""
        echo "🐧 Setting up Linux environment..."
        
        # Install system dependencies for buildozer
        echo "Installing system dependencies..."
        sudo apt-get update
        sudo apt-get install -y \
            build-essential \
            git \
            python3-dev \
            ffmpeg \
            libsdl2-dev \
            libsdl2-image-dev \
            libsdl2-mixer-dev \
            libsdl2-ttf-dev \
            libportmidi-dev \
            libswscale-dev \
            libavformat-dev \
            libavcodec-dev \
            zlib1g-dev \
            libgstreamer1.0 \
            gstreamer1.0-plugins-base \
            gstreamer1.0-plugins-good
        
        echo "✅ Linux setup complete"
        ;;
    
    # macOS setup
    darwin*)
        echo ""
        echo "🍎 Setting up macOS environment..."
        
        # Check if Homebrew is installed
        if ! command_exists brew; then
            echo "Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        
        # Install dependencies
        brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
        
        # iOS-specific setup
        echo "Installing iOS build tools..."
        $PIP_CMD install kivy-ios
        
        echo "✅ macOS setup complete"
        echo "📱 For iOS builds, ensure you have Xcode installed from the App Store"
        ;;
    
    # Windows/MSYS setup
    msys*|cygwin*)
        echo ""
        echo "🪟 Windows environment detected"
        echo "⚠️  For best results, consider using WSL (Windows Subsystem for Linux)"
        echo "Building Android apps on Windows can be challenging"
        ;;
    
    *)
        echo "Unknown operating system: $OSTYPE"
        echo "Please refer to Kivy documentation for your platform"
        ;;
esac

# Install buildozer
echo ""
echo "🔨 Installing buildozer..."
$PIP_CMD install --upgrade buildozer

# Create .buildozer directory
mkdir -p ~/.buildozer

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. To build for Android: ./build_android.sh (Linux/WSL) or .\build_android.ps1 (Windows)"
echo "2. To build for iOS: ./build_ios.sh (macOS only)"
echo "3. Test the app: python main.py"
echo ""
echo "For first-time Android builds, buildozer will download additional"
echo "dependencies (Android SDK, NDK) which may take some time."

# Make build scripts executable
chmod +x build_android.sh 2>/dev/null || true
chmod +x build_ios.sh 2>/dev/null || true

echo ""
echo "Happy coding! 🐌🏁"