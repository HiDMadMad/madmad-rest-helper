# Lehaam | لِهام
A simple and smart Python app to help you optimize your sleep and nap schedules.  
whether you're planning your nightly sleep or a quick daytime nap, this app calculates the best times to sleep and wake up for maximum rest and productivity.

[![Version](https://img.shields.io/badge/version-1.0.0-green)](https://github.com/HiDMadMad/Lehaam/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-yellow)](https://www.python.org/downloads/)

---

## Features
- ⏱️ calculates ideal sleep and wake-up times based on sleep cycles  
- 🌙 supports both nighttime sleep and daytime naps ☀️  
- 💻 Simple CLI interface for local use  
- 🤖 telegram bot for sleep suggestions on the go  
- 👍 user-friendly and easy to use  
- ⚡ helps improve your overall rest and energy levels  

---

## How It Works ❓
sleep happens in cycles of approximately 90 minutes. waking up between these cycles (rather than in the middle of one) helps you feel refreshed and energized.  
**Lehaam** calculates optimal times to fall asleep and wake up for better rest.
- 90-minute sleep cycles
- 15 minutes average time to fall asleep
- recommended 4-6 complete sleep cycles per night (6-9 hours)

---

## Installation
### 🤖 Telegram Bot
 click on [lehaambot](https://t.me/lehaambot) or go to the telegram and search for `lehaambot` to start using it instantly!  
 don't worry, it's user-friendly =)

### 🖱️ Quick Start (Windows)
1. download the latest release: [**Lehaam-v1.0.0.exe**](https://github.com/HiDMadMad/Lehaam/releases/latest)
2. double-click to run
3. no installation required!

### ⌨️ Run from Source
```bash
# clone the repository
git clone https://github.com/HiDMadMad/Lehaam.git
cd Lehaam

# install dependencies
pip install -r requirements.txt

# run the CLI app
python src/cli/cli_app.py
```

---

## Project Structure
```
Lehaam/
├── assets/
│   ├── img.png                     # application icon (png)
│   └── lehaam_icon.ico             # application icon (ico)
│
├── src/
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── cli_app.py              # CLI application
│   │   ├── cli_messages.py         # CLI UI messages and text
│   │   └── update_cli_exe_app.py   # CLI .exe updater
│   │
│   ├── telegram-bot/
│   │   ├── __init__.py
│   │   ├── telegram_bot.py         # telegram bot
│   │   ├── bot_messages.py         # bot UI messages and text
│   │   ├── bot_handlers.py         # bot handlers
│   │   └── user_storage.py         # lehaam telegram users
│   │
│   ├── __init__.py
│   └── lehaam_pieces.py            # core logic and calculations
│
├── .gitignore
├── LICENSE
├── README.md                       # this file
└── requirements.txt                # dependencies
```

---

## Contributions
**feedback, ideas, and pull requests are welcome!**  
**feel free to open an issue or contribute.**

### here's how you can help :
1. 🐛 report bugs by [opening an issue](https://github.com/HiDMadMad/Lehaam/issues)
2. 💡 suggest new features or improvements
3. 🔧 submit pull requests with bug fixes or enhancements
4. 📖 improve documentation
5. ...
#### development setup :
```bash
git clone https://github.com/HiDMadMad/Lehaam
cd Lehaam
pip install -r requirements.txt
```

---

## Support
if you find Lehaam helpful, please consider :
- ⭐ starring the repository
- 🐛 reporting bugs
- 💬 sharing with friends who need better sleep!

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
**Copyright © 2025 [HiDMadMad](https://github.com/HiDMadMad)**

---

## Contact
- Telegram : [@OxMadMad](OxMadMad.t.me)
- LinkedIn : [mohammad-reza-rahmanian](https://www.linkedin.com/in/mohammad-reza-rahmanian)
- Email : [madmadpv@gmail.com](mailto:madmadpv@gmail.com)

---

<div align="center">
made with ❤️ for better sleep
</div>

---
