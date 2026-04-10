# 🐱 Bongo Cat Auto-Clicker

![Python Version](https://img.shields.io/badge/python-3.14%2B-blue)
![Framework](https://img.shields.io/badge/framework-pydirectinput-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

A Python script designed to simulate ultra-fast drumming for Bongo Cat desktop app. Unlike standard clickers, this uses hardware-level input simulation to ensure the app registers every single hit.

## ✨ Features

- **Braille UI:** ASCII art to improve the terminal interface.
- **Dual-Input Simulation:** Alternates between left and right paws for a realistic drumming effect.
- **Speed:** Capable of 50+ hits per second (adjustable).
- **Safe Toggle:** Start combo to prevent accidental activation.
- **Stop Button:** Instant stop with a single keypress.

### 📽️ Demo

<p align="center">
  <img src="demo.gif" alt="Bongo Cat Drumming">
</p>

## 🛠️ Setup

1.  **Install Python:** Download the official [Python](https://www.python.org/) installer. **Make sure to check "Add Python to PATH" during installation.**
2.  **Install Dependencies:** Open your terminal in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Permissions:** Because this script interacts with other windows, you **must** run your code editor (VS Code) as **Administrator**.
4.  **Run the Script:** Open `main.py` in VS Code and press the **Play Button** in the top right or hit `CTRL` + `F5`.

## 🎮 Controls

| Action             | Key Combination            |
| :----------------- | :------------------------- |
| **Start Drumming** | `CTRL` + `F8`              |
| **Stop Drumming**  | `ESC`                      |
| **Exit Program**   | `ESC` (while not drumming) |

> [TIP]
> **For best results:** Open a Notepad app and make sure it is your current active window. As shown in the demo GIF, this script types `a` and `d` rapidly; having a text document active prevents the script from accidentally triggering shortcuts in other applications.

## ⚙️ Customization

You can tweak the performance by opening `main.py` and changing these values:

- `SPEED`: Lower numbers = faster drumming (e.g., `0.005` for extreme speed).
- `LEFT_PAW` / `RIGHT_PAW`: Change these if you want to uses different keys.

## ⚠️ Troubleshooting

- **Cat isn't moving?** Ensure the Bongo Cat window is the "Active" window (click on it) before starting the combo.
- **Keys not registering?** Make sure you ran your terminal/VS Code as **Administrator**. Windows blocks non-admin scripts from sending inputs to other apps for security.

---

_Maintained with ❤️ for the Bongo Cat community._
