#!/usr/bin/env python3

import os
import json
from datetime import datetime

# --- Configuration ---
HISTORY_FILE = os.path.expanduser("~/.commandmaster_history.json")
# --- ANSI Color Codes ---
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def get_shell_config_file():
    """Detects the user's shell and returns the appropriate config file."""
    shell = os.environ.get("SHELL", "")
    if "zsh" in shell:
        return os.path.expanduser("~/.zshrc")
    else:
        # Default to .bashrc for bash and other shells
        return os.path.expanduser("~/.bashrc")

def display_menu():
    """Prints the main menu of the tool."""
    print("\n" + "="*5 + " CommandMaster " + "="*5)
    print("1. Create a custom command")
    print("2. Remove a custom command")
    print("3. History of all custom commands")
    print("4. Update old custom command")
    print("5. About")
    print("6. Exit")
    print("-" * 27)

def load_history():
    """Loads the command history from the JSON file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r') as f:
        return json.load(f)

def save_history(history):
    """Saves the command history to the JSON file."""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def create_command():
    """Creates a new custom command."""
    name = input("Enter command name: ")
    action = input("Enter command action: ")
    history = load_history()

    # Check for existing command
    for command in history:
        if command["name"] == name:
            print(f"{YELLOW}Command '{name}' already exists. Use option 4 to update.{RESET}")
            return

    # Add to shell config
    config_file = get_shell_config_file()
    with open(config_file, "a") as f:
        f.write(f"\nalias {name}='{action}' # Added by CommandMaster\n")

    # Add to history
    history.append({
        "name": name,
        "action": action,
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_history(history)
    print(f"{GREEN}✅ Command '{name}' added successfully!{RESET}")
    print("Please restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to use the new command.")

def remove_command():
    """Removes an existing custom command."""
    history = load_history()
    if not history:
        print(f"{YELLOW}No commands in history to remove.{RESET}")
        return

    print("Select a command to remove:")
    for i, command in enumerate(history):
        print(f"{i + 1}. {command['name']}")

    try:
        choice = int(input("Enter your choice: ")) - 1
        if not 0 <= choice < len(history):
            print(f"{RED}Invalid choice.{RESET}")
            return
    except ValueError:
        print(f"{RED}Invalid input.{RESET}")
        return

    command_to_remove = history[choice]
    name = command_to_remove["name"]

    confirm = input(f"Are you sure you want to remove '{name}'? [y/N]: ").lower()
    if confirm != 'y':
        print("Removal cancelled.")
        return

    # Remove from shell config
    config_file = get_shell_config_file()
    with open(config_file, "r") as f:
        lines = f.readlines()
    with open(config_file, "w") as f:
        for line in lines:
            if not line.strip().startswith(f"alias {name}="):
                f.write(line)

    # Remove from history
    history.pop(choice)
    save_history(history)
    print(f"{GREEN}✅ Command '{name}' removed successfully!{RESET}")
    print("Please restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to apply the changes.")

def view_history():
    """Displays the history of all custom commands."""
    history = load_history()
    if not history:
        print(f"{YELLOW}No commands in history to display.{RESET}")
        return

    print("\n" + "="*5 + " Command History " + "="*5)
    for command in history:
        print(f"Name: {command['name']}")
        print(f"Action: {command['action']}")
        print(f"Date Created: {command['date_created']}")
        print("-" * 27)

def update_command():
    """Updates an existing custom command."""
    history = load_history()
    if not history:
        print(f"{YELLOW}No commands in history to update.{RESET}")
        return

    print("Select a command to update:")
    for i, command in enumerate(history):
        print(f"{i + 1}. {command['name']}")

    try:
        choice = int(input("Enter your choice: ")) - 1
        if not 0 <= choice < len(history):
            print(f"{RED}Invalid choice.{RESET}")
            return
    except ValueError:
        print(f"{RED}Invalid input.{RESET}")
        return

    command_to_update = history[choice]
    name = command_to_update["name"]
    new_action = input(f"Enter the new action for '{name}': ")

    confirm = input(f"Are you sure you want to update '{name}'? [y/N]: ").lower()
    if confirm != 'y':
        print("Update cancelled.")
        return

    # Update shell config
    config_file = get_shell_config_file()
    with open(config_file, "r") as f:
        lines = f.readlines()
    with open(config_file, "w") as f:
        for line in lines:
            if line.strip().startswith(f"alias {name}="):
                f.write(f"alias {name}='{new_action}' # Updated by CommandMaster\n")
            else:
                f.write(line)

    # Update history
    history[choice]["action"] = new_action
    save_history(history)
    print(f"{GREEN}✅ Command '{name}' updated successfully!{RESET}")
    print("Please restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to apply the changes.")

def about():
    """Displays information about the tool."""
    print("\n" + "="*5 + " About CommandMaster " + "="*5)
    print("Version: 1.0")
    print("Developed by: Nabin Sharma")
    print("Website: www.nabinsharma329.com.np")
    print("=" * 31)

def main():
    """The main function of the program."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_command()
        elif choice == '2':
            remove_command()
        elif choice == '3':
            view_history()
        elif choice == '4':
            update_command()
        elif choice == '5':
            about()
        elif choice == '6':
            print("Exiting CommandMaster. Goodbye!")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
