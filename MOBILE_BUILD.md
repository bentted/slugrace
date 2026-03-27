# SlugRace Mobile App Documentation 📱🐌

This document explains how to build and deploy SlugRace as mobile applications for Android and iOS.

## 🎯 Overview

SlugRace has been converted to support mobile platforms while maintaining all original functionality:

- **Cross-platform**: Works on Android, iOS, and desktop
- **Responsive UI**: Automatically adapts to different screen sizes
- **Touch-optimized**: Larger buttons and touch targets for mobile
- **Mobile features**: Haptic feedback (vibration) support
- **Performance optimized**: Efficient resource usage for mobile devices

## 📋 Prerequisites

### For Android Development:
- **Linux (recommended)** or **WSL on Windows**
- Python 3.8 or later
- Git
- Java JDK 8 or 11
- Buildozer will automatically download Android SDK/NDK

### For iOS Development:
- **macOS only**
- Xcode (from App Store)
- Python 3.8 or later
- Apple Developer account (for device testing)

## 🚀 Quick Start

### 1. Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/bentted/slugrace.git
cd slugrace

# Run the automated setup script
chmod +x setup_mobile.sh
./setup_mobile.sh
```

### 2. Test Desktop Version

```bash
# Install requirements
pip install -r requirements.txt

# Test the game
python main.py
```

### 3. Build for Mobile

#### Android Build:
```bash
# Linux/WSL
./build_android.sh

# Windows PowerShell
.\build_android.ps1
```

#### iOS Build:
```bash
# macOS only
./build_ios.sh
```

## 📱 Mobile-Specific Features

### Responsive Design
- **Finish line**: Automatically adjusts to 80% of screen width
- **Touch targets**: Buttons are enlarged for better mobile interaction
- **Font sizes**: Text scales appropriately for mobile screens
- **Layouts**: Spacing and sizing adapt to screen dimensions

### Haptic Feedback
The app provides vibration feedback for:
- Race start events
- Race finish events
- Button interactions
- Game over events

Enable/disable in game settings or modify `vibration_enabled` property.

### Screen Orientation
- **Portrait mode**: Optimized layout for phone usage
- **Landscape mode**: Traditional racing view for tablets
- **Auto-rotation**: Responds to device orientation changes

## 🔧 Build Configuration

### Android Configuration (buildozer.spec)

Key settings you can modify:

```ini
[app]
title = SlugRace
package.name = slugrace
package.domain = org.slugrace
version = 1.0

# Permissions
android.permissions = VIBRATE,WAKE_LOCK

# Architecture (choose one)
android.arch = armeabi-v7a  # 32-bit ARM (older devices)
# android.arch = arm64-v8a  # 64-bit ARM (modern devices)
# android.arch = x86_64     # Intel/AMD (emulators)

# Graphics
fullscreen = 1
```

### iOS Configuration
iOS builds use Xcode project generation. Key files:
- `buildozer.spec` - Main configuration
- Xcode project in `platforms/ios/` after build

## 📦 Build Outputs

### Android
- **Debug APK**: `bin/slugrace-1.0-debug.apk`
- **Release APK**: `bin/slugrace-1.0-release.apk` (when building release)

### iOS
- **Xcode Project**: `platforms/ios/`
- **IPA file**: Generated through Xcode

## 📲 Installation

### Android Installation Options:

1. **ADB Install**:
   ```bash
   adb install bin/slugrace-1.0-debug.apk
   ```

2. **Manual Install**:
   - Transfer APK to device
   - Enable "Unknown Sources" in Settings
   - Tap APK file to install

3. **Google Play Store**:
   - Build release APK/AAB
   - Upload to Play Console

### iOS Installation Options:

1. **Development**:
   - Open Xcode project
   - Connect device
   - Build & Run

2. **TestFlight**:
   - Archive in Xcode
   - Upload to App Store Connect
   - Distribute via TestFlight

3. **App Store**:
   - Submit for review through App Store Connect

## 🐛 Troubleshooting

### Common Android Issues:

**Build fails with Java errors**:
```bash
# Install correct Java version
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

**NDK/SDK download issues**:
```bash
# Clear buildozer cache
buildozer android clean
rm -rf ~/.buildozer
```

**Permission errors**:
- Ensure user has write permissions to project directory
- On Windows, run as administrator or use WSL

### Common iOS Issues:

**Code signing errors**:
- Configure signing in Xcode
- Ensure Apple Developer account is active

**Deployment target too low**:
- Update iOS deployment target in Xcode project settings

**Missing dependencies**:
```bash
# Reinstall iOS build tools
pip uninstall kivy-ios
pip install kivy-ios
```

### General Issues:

**App crashes on startup**:
- Check device logs: `adb logcat` (Android) or Xcode console (iOS)
- Ensure all audio files are accessible
- Verify asset file paths

**UI elements too small/large**:
- Modify `mobile_responsive.kv` font sizes and dimensions
- Test on different screen densities

**Performance issues**:
- Reduce audio file sizes
- Optimize image assets
- Enable hardware acceleration in buildozer.spec

## 📁 Project Structure

```
slugrace/
├── main.py                 # Main application file (mobile-enhanced)
├── buildozer.spec         # Android build configuration
├── requirements.txt       # Python dependencies
├── mobile_responsive.kv   # Mobile UI adjustments
├── setup_mobile.sh        # Development setup script
├── build_android.sh       # Android build script (Linux/WSL)
├── build_android.ps1      # Android build script (Windows)
├── build_ios.sh           # iOS build script (macOS)
├── assets/                # Game assets (audio, images)
└── [other game files]     # Original game modules
```

## 🔄 Updates and Versioning

To release updates:

1. **Update version** in `buildozer.spec`:
   ```ini
   version = 1.1
   ```

2. **Clean and rebuild**:
   ```bash
   buildozer android clean
   buildozer android release  # For production
   ```

3. **Test thoroughly** on multiple devices and screen sizes

## 🆘 Getting Help

- **Buildozer Issues**: [Kivy Documentation](https://buildozer.readthedocs.io/)
- **Kivy Mobile Support**: [Kivy Garden](https://github.com/kivy-garden)
- **Android Specific**: [Python-for-Android](https://github.com/kivy/python-for-android)
- **iOS Specific**: [Kivy-iOS](https://github.com/kivy/kivy-ios)

## 🎉 Success!

Once built successfully, your SlugRace mobile app will have all the original desktop functionality optimized for mobile devices:

- ✅ Touch-friendly interface
- ✅ Responsive design for all screen sizes
- ✅ Mobile-optimized performance
- ✅ Haptic feedback support
- ✅ Full-screen experience
- ✅ All original game features intact

Happy racing! 🐌🏁📱