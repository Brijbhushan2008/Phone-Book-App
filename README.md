# Phone Book App

A small, menu-driven command-line phone book written in Python. It lets you add contacts, look up a contact by name, list saved contacts, and delete entries—all through prompts in the terminal.

## Features

- **Add a contact:** enter a name and phone number to add it to the phone book.
- **Search contacts:** look up a saved number using the contact's full name.
- **View all contacts:** display the contacts currently stored while the program is running.
- **Delete a contact:** remove a contact by entering its name.
- **Simple interactive menu:** keep using the phone book until you choose Exit.

## Requirements

- Python 3
- No third-party Python packages are required; the script uses the Python standard library.

## Run the app

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python Phone_Book_app.py
```

On some systems, the command may be `python3 Phone_Book_app.py`.

## How to use it

Choose an option from the menu:

```text
1. ADD
2. SEARCH
3. VIEW ALL
4. DELETE
5. EXIT
```

For **Add**, enter the contact name and phone number. For **Search** and **Delete**, enter the name exactly as it was saved. Choose **View All** to see the contacts currently in memory, or **Exit** to close the program.

## Data and limitations

Contacts are stored in a Python dictionary while the program is running. They are not written to a file or database, so the phone book starts empty again after the application exits. Names are used as dictionary keys; adding another contact with the same name replaces the previous number. The current version is a beginner-friendly terminal project and does not yet validate phone-number formats or persist contacts between sessions.

## Built with

- Python 3
- Standard library: `time` and `os`

## Learning goals

This project practices Python dictionaries, loops, conditionals, console input/output, and basic CRUD-style operations (create, read, and delete contacts).
