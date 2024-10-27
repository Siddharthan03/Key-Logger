# Key-Logger
## Overview

This Keylogger project is designed to capture keystrokes from a user’s keyboard and log them for monitoring and analysis. It serves as an educational tool to understand the functionality of keyloggers and their potential security implications.

## Features

- **Keystroke Logging**: Captures every keystroke made by the user.
- **Timestamped Logs**: Each logged keystroke is timestamped for accurate tracking.
- **Data Storage**: Logs can be stored in a local text file for easy access and review.
- **Cross-Platform Compatibility**: Designed to work on Windows, macOS, and Linux systems.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `pynput` for capturing keyboard events
  - `datetime` for timestamping logs
- **Version Control**: Git

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger
   pip install pynput
   python keylogger.py
## Usage
- Launch the application to start logging keystrokes.
- The keystrokes will be logged in a file named keylog.txt.
- Stop the application to end logging. The final log file will contain all captured keystrokes.
  
## Important Note
This project is intended for educational purposes only. Unauthorized use of keyloggers can violate privacy rights and local laws. Always ensure that you have permission before logging keystrokes on any device.
