#!/bin/bash

# SlugRace Mobile Build Environment Test Script
# This script verifies that your environment is properly set up for mobile builds

echo "🐌 SlugRace Mobile Build Environment Test"
echo "========================================"

ERRORS=0
WARNINGS=0

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to print status
print_status() {
    if [ "$2" = "OK" ]; then
        echo "✅ $1"
    elif [ "$2" = "WARN" ]; then
        echo "⚠️  $1"
        ((WARNINGS++))
    else
        echo "❌ $1"
        ((ERRORS++))
    fi
}

echo ""
echo "📋 Checking Basic Requirements..."

# Check Python
if command_exists python3; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    print_status "Python 3 found: $PYTHON_VERSION" "OK"
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command_exists python; then
    PYTHON_VERSION=$(python --version 2>&1 | cut -d' ' -f2)
    if [[ $PYTHON_VERSION =~ ^3\. ]]; then
        print_status "Python found: $PYTHON_VERSION" "OK"
        PYTHON_CMD=python
        PIP_CMD=pip
    else
        print_status "Python 2.x detected: $PYTHON_VERSION (Python 3.8+ required)" "ERROR"
        PYTHON_CMD=""
    fi
else
    print_status "Python not found" "ERROR"
    PYTHON_CMD=""
fi

# Check pip
if [ ! -z "$PYTHON_CMD" ] && command_exists $PIP_CMD; then
    print_status "pip found" "OK"
else
    print_status "pip not found" "ERROR"
fi

# Check Git
if command_exists git; then
    print_status "Git found" "OK"
else
    print_status "Git not found (recommended for development)" "WARN"
fi

echo ""
echo "📦 Checking Python Dependencies..."

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    print_status "requirements.txt found" "OK"
    
    # Check if dependencies are installed
    if [ ! -z "$PYTHON_CMD" ]; then
        echo "   Checking installed packages..."
        
        if $PYTHON_CMD -c "import kivy" 2>/dev/null; then
            KIVY_VERSION=$($PYTHON_CMD -c "import kivy; print(kivy.__version__)" 2>/dev/null)
            print_status "   Kivy: $KIVY_VERSION" "OK"
        else
            print_status "   Kivy not installed" "ERROR"
        fi
        
        if $PYTHON_CMD -c "import buildozer" 2>/dev/null; then
            print_status "   Buildozer installed" "OK"
        else
            print_status "   Buildozer not installed (needed for Android builds)" "WARN"
        fi
        
        if $PYTHON_CMD -c "import plyer" 2>/dev/null; then
            print_status "   Plyer installed (mobile features)" "OK"
        else
            print_status "   Plyer not installed (mobile features unavailable)" "WARN"
        fi
    fi
else
    print_status "requirements.txt not found" "ERROR"
fi

echo ""
echo "🏗️ Checking Build Environment..."

# Platform-specific checks
case "$OSTYPE" in
    linux-gnu*)
        echo "   Platform: Linux ✅"
        
        # Check for Android build dependencies
        if command_exists java; then
            JAVA_VERSION=$(java -version 2>&1 | head -n1 | cut -d'"' -f2)
            print_status "   Java: $JAVA_VERSION" "OK"
        else
            print_status "   Java not found (required for Android builds)" "ERROR"
        fi
        
        # Check for common build tools
        if command_exists make; then
            print_status "   Build tools (make) found" "OK"
        else
            print_status "   Build tools missing" "ERROR"
        fi
        ;;
        
    darwin*)
        echo "   Platform: macOS ✅"
        
        # Check Java for Android builds
        if command_exists java; then
            print_status "   Java found (for Android builds)" "OK"
        else
            print_status "   Java not found (install for Android builds)" "WARN"
        fi
        
        # Check Xcode for iOS builds
        if command_exists xcodebuild; then
            XCODE_VERSION=$(xcodebuild -version 2>/dev/null | head -n1)
            print_status "   Xcode: $XCODE_VERSION" "OK"
        else
            print_status "   Xcode not found (required for iOS builds)" "WARN"
        fi
        
        # Check for iOS build tools
        if $PYTHON_CMD -c "import kivy_ios" 2>/dev/null; then
            print_status "   kivy-ios installed" "OK"
        else
            print_status "   kivy-ios not installed (for iOS builds)" "WARN"
        fi
        ;;
        
    msys*|cygwin*)
        echo "   Platform: Windows"
        print_status "   Consider using WSL for better Android build support" "WARN"
        ;;
        
    *)
        echo "   Platform: Unknown ($OSTYPE)"
        print_status "   Platform may not be supported" "WARN"
        ;;
esac

echo ""
echo "📁 Checking Project Files..."

# Check for essential files
essential_files=("main.py" "buildozer.spec" "mobile_responsive.kv")
for file in "${essential_files[@]}"; do
    if [ -f "$file" ]; then
        print_status "$file exists" "OK"
    else
        print_status "$file missing" "ERROR"
    fi
done

# Check for build scripts
build_scripts=("build_android.sh" "build_ios.sh" "setup_mobile.sh")
for script in "${build_scripts[@]}"; do
    if [ -f "$script" ]; then
        if [ -x "$script" ]; then
            print_status "$script exists and is executable" "OK"
        else
            print_status "$script exists but not executable" "WARN"
            echo "   Fix with: chmod +x $script"
        fi
    else
        print_status "$script missing" "ERROR"
    fi
done

# Check assets directory
if [ -d "assets" ]; then
    asset_count=$(find assets -type f | wc -l)
    print_status "Assets directory found ($asset_count files)" "OK"
else
    print_status "Assets directory missing" "ERROR"
fi

echo ""
echo "🎮 Testing Game Launch..."

if [ ! -z "$PYTHON_CMD" ] && [ -f "main.py" ]; then
    # Quick syntax check
    if $PYTHON_CMD -m py_compile main.py 2>/dev/null; then
        print_status "main.py syntax is valid" "OK"
    else
        print_status "main.py has syntax errors" "ERROR"
    fi
    
    # Test import of main modules
    if $PYTHON_CMD -c "
import sys
sys.path.insert(0, '.')
try:
    from main import Game, SlugraceApp
    print('SUCCESS: Main modules import correctly')
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)
" 2>/dev/null; then
        print_status "Main modules import successfully" "OK"
    else
        print_status "Module import errors detected" "ERROR"
    fi
else
    print_status "Cannot test game launch (Python or main.py unavailable)" "ERROR"
fi

echo ""
echo "📊 Test Results Summary"
echo "======================"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "🎉 Perfect! Your environment is fully set up for SlugRace mobile development!"
    echo ""
    echo "🚀 Ready to build:"
    echo "   Android: ./build_android.sh"
    echo "   iOS: ./build_ios.sh (macOS only)"
    echo "   Desktop test: python main.py"
    
elif [ $ERRORS -eq 0 ]; then
    echo "✅ Good! Your environment is mostly ready with $WARNINGS warnings"
    echo "   You can proceed with builds, but consider addressing the warnings"
    
else
    echo "❌ Issues found: $ERRORS errors, $WARNINGS warnings"
    echo "   Please fix the errors before attempting mobile builds"
    echo ""
    echo "💡 Common fixes:"
    echo "   - Install missing dependencies: pip install -r requirements.txt"
    echo "   - Run setup script: ./setup_mobile.sh"
    echo "   - Install Java JDK for Android builds"
    echo "   - Install Xcode for iOS builds (macOS only)"
fi

echo ""
exit $ERRORS