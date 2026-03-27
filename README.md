

---

# SlugRace 🐌📱

**SlugRace** is an exciting and fun Python-based game built using the [Kivy](https://kivy.org) framework. It combines Python and KvLang to deliver an engaging racing experience where players bet on slugs and watch them race to victory!

**🆕 Now Available on Mobile!** SlugRace has been converted to run on Android and iOS devices with full functionality and mobile-optimized UI.

---

## Features

- **📱 Cross-Platform**: Available on Desktop, Android, and iOS
- **🎮 Interactive Betting System**: Place bets on your favorite slug and see if they win the race
- **🏁 Dynamic Gameplay**: Real-time slug racing simulations with randomized results
- **📲 Mobile-Optimized**: Touch-friendly interface with responsive design
- **🎵 Rich Audio Experience**: Background music and sound effects
- **📳 Mobile Features**: Haptic feedback (vibration) support
- **⚙️ Customizable Settings**: Tailor the game to your preferences
- **🔧 Modular Design**: Organized codebase with reusable components

---

## Repository Structure

| File/Folder          | Description                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| `main.py`            | The entry point for the game, containing the primary logic and application lifecycle.         |
| `accident.py`        | Handles random events or accidents occurring during the race.                                 |
| `bets.py`            | Manages the betting system, allowing users to place bets on their chosen slugs.               |
| `race.py`            | Contains the logic for simulating slug races.                                                 |
| `settings.py`        | Configuration file for game settings and user preferences.                                    |
| `widgets.py`         | Custom widgets used throughout the game interface.                                            |
| `.kv` Files          | Define the UI structure and design using KvLang.                                              |
| `assets/`            | Directory for game assets such as images, sounds, or other media.                             |
| `__pycache__/`       | Auto-generated directory for Python bytecode files.                                           |

---

## How to Run

### Desktop Version

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bentted/slugrace.git
   cd slugrace
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**:
   ```bash
   python main.py
   ```

### Mobile Versions

#### 📱 Quick Mobile Setup:
```bash
# Automated setup for mobile development
chmod +x setup_mobile.sh
./setup_mobile.sh
```

#### 🤖 Android Build:
```bash
# Linux/WSL
./build_android.sh

# Windows PowerShell  
.\build_android.ps1
```

#### 🍎 iOS Build (macOS only):
```bash
./build_ios.sh
```

**📚 For detailed mobile build instructions, see [MOBILE_BUILD.md](MOBILE_BUILD.md)**

---

## Technologies Used

- **Python (55.8%)**: The primary programming language used for game logic and backend systems
- **KvLang (44.2%)**: Used to create responsive and visually appealing user interfaces  
- **Kivy Framework**: Cross-platform app development framework
- **Buildozer**: Android app packaging and build tool
- **Kivy-iOS**: iOS app development and packaging tool

### Supported Platforms:
- 🖥️ **Desktop**: Windows, macOS, Linux
- 🤖 **Android**: Version 5.0+ (API 21+)
- 🍎 **iOS**: Version 11.0+

---

## Contribution

Contributions are welcome! If you’d like to contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## Fun Fact

Did you know? Slugs can stretch to 20 times their normal length when racing (in this game, at least)!

---

### [View More Files in the Repository](https://github.com/bentted/slugrace)

