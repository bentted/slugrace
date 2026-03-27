#!/bin/bash

# Make all shell scripts executable for SlugRace mobile development

echo "🔧 Setting up SlugRace mobile development scripts..."

# List of scripts to make executable
scripts=(
    "setup_mobile.sh"
    "build_android.sh" 
    "build_ios.sh"
    "test_mobile_setup.sh"
)

# Make scripts executable
for script in "${scripts[@]}"; do
    if [ -f "$script" ]; then
        chmod +x "$script"
        echo "✅ Made $script executable"
    else
        echo "⚠️  $script not found"
    fi
done

echo ""
echo "🎉 Script setup complete!"
echo ""
echo "Next steps:"
echo "1. Run setup: ./setup_mobile.sh"
echo "2. Test setup: ./test_mobile_setup.sh"  
echo "3. Build Android: ./build_android.sh"
echo "4. Build iOS: ./build_ios.sh (macOS only)"

echo ""