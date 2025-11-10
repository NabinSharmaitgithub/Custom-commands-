# 🧠 CommandMaster — Custom Command Creator for Linux

**CommandMaster** is a Python-based interactive CLI tool that helps you **create, manage, and track custom Linux commands** effortlessly.  
Whether you’re using **Ubuntu**, **Kali Linux**, **Arch**, or even **Termux**, this tool makes command customization simple and safe.

---

## 🚀 Features

| Option | Description |
|:--|:--|
| **1. Create a custom command** | Add new custom commands or aliases easily — automatically updates your shell config (`.bashrc`, `.zshrc`, etc.). |
| **2. Remove a custom command** | Remove unwanted commands from both your shell and command history. |
| **3. View command history** | View all commands you’ve created with timestamps. |
| **4. Update existing commands** | Edit and modify any previously created command. |
| **5. About** | Displays developer information and website link. |
| **6. Exit** | Cleanly exits the application. |

---

## 🧩 How It Works

CommandMaster automatically:
- Detects your current shell (e.g., Bash or Zsh).  
- Updates your configuration file (`~/.bashrc`, `~/.zshrc`, etc.) safely.  
- Tracks all command creations and updates in a JSON file (`~/.commandmaster_history.json`).  
- Works on any Linux environment — including **Termux** on Android.

---

## ⚙️ Requirements

- **Python 3.x**  
- Standard libraries only (`os`, `json`, `datetime`, etc.)  
- Optional: `colorama` for colored output (auto-detected if available)

---

## 🧠 Installation

```bash
# Clone the repository
git clone https://github.com/username/CommandMaster.git
cd CommandMaster

# Run the tool
python3 commandmaster.py

If you’re using Termux, make sure Python is installed:

pkg install python -y


---

## 💡 Example Usage

$ python3 commandmaster.py

=== CommandMaster ===
1. Create a custom command
2. Remove a custom command
3. History of all custom commands
4. Update old custom command
5. About
6. Exit
-----------------------------

Enter your choice: 1
Enter command name: greet
Enter command action: echo "Hello, $USER!"
✅ Command 'greet' added successfully!

$ greet
Hello, nabin


---

## 🧾 Data Storage

Shell Config File:
Stores your command as an alias or function.

History File:
~/.commandmaster_history.json keeps a record of all added, updated, and removed commands.



---

## 📘 About

Developer: Nabin Sharma
Website: www.nabinsharma329.com.np
Project Name: CommandMaster
Version: 1.0.0
License: MIT License


---

## 🛠️ Future Improvements

Add global command sharing (export/import).

GUI version for desktop Linux.

Auto-sync feature between devices.



---

## ❤️ Contributing

Pull requests are welcome!
If you’d like to improve this tool, fix a bug, or add new features, please fork the repository and submit a PR.


---

## 🧾 License

This project is licensed under the MIT License — feel free to use and modify it as you like.


---

© 2025 Nabin Sharma — www.nabinsharma329.com.np

---
totoottoottoottoottoottoottoottoottoottoottoottoottoottoottoottoottooaal
