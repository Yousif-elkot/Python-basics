# Python Learning Journey 🚀

This repository documents my **30-day Python & Cloud Engineering journey**, where I build small projects and steadily improve them.  
Each day introduces a new concept, and over time the projects grow in complexity and quality.

The goal is to strengthen my Python foundations while practicing Git/GitHub workflows, documentation, and professional coding habits — all essential skills for a future Cloud Engineer.

---

## 📅 Day 1 — Unit Converter

### 🎯 Objective

Build a simple **command-line program** that converts between common units.  
This exercise focuses on:

- Writing basic Python scripts
- Handling user input/output
- Applying arithmetic formulas
- Using `if/elif/else` control flow

---

### ✅ Version 1 (Initial)

- CLI menu with 4 conversion options:
  - Kilometers ↔ Miles
  - Celsius ↔ Fahrenheit
- Program performs **one conversion per run**.
- Demonstrates:
  - `input()` for user input
  - `print()` for formatted output
  - Arithmetic operators for conversion formulas
  - Branching with `if/elif/else`

---

### 🔧 Version 2 (Improvements)

- Added a **loop** so users can perform multiple conversions in one run.
- Introduced an **exit option** (`q` to quit).
- Added **input validation** for menu selection (handles invalid choices gracefully).
- Code is more user-friendly and closer to real-world CLI tools.

---

### 📚 Learning Outcomes

- Reinforced the concept of **control flow** in Python.
- Practiced structuring small programs for clarity and scalability.
- Understood how to iterate on an initial solution, improving usability step by step.
- Gained confidence in using Git to track project versions (commit history shows progress).

---

### 🚀 Next Planned Improvements

- Break the code into **modular functions** for better readability.
- Add **unit tests** to verify conversions.
- Explore handling **edge cases** (e.g., non-numeric input).
- Possibly extend with more unit categories (weight, time, etc.).

---

📱 Phone Book CLI Application
🎯 Objective

Build a command-line phone book application to manage contacts.
This project introduces:

Working with Python dictionaries for data storage

Using the json module for persistence

Handling user input validation

Structuring a basic menu-driven CLI program

✅ Version 1 (Initial)

Features:

Add new contacts (name + phone number)

Search contacts by name

Delete contacts with confirmation

List all contacts in a clean format

Save contacts automatically to my_contacts.json

Demonstrates:

Dictionary operations (add, search, delete)

File I/O with json.dump() and json.load()

Exception handling with try/except (FileNotFoundError)

Loops and branching (while, if/elif/else)

🔧 Version 2 (Planned Improvements)

Refactor code into functions (add_contact(), search_contact(), etc.) for clarity.

Add ability to edit/update contacts.

Store multiple fields per contact (e.g., email, address).

Export/import contacts (CSV or SQLite database).

Enhance input validation (e.g., valid phone number format).

📚 Learning Outcomes

Learned how to build persistent CLI tools with Python.

Practiced separating program logic from data storage.

Reinforced error handling and input validation concepts.

Strengthened Git/GitHub skills by documenting iterations with commits.

🚀 Next Steps

Explore modularization (splitting code into multiple files).

Add unit tests for reliability.

Consider creating a GUI version using Tkinter or PyQt.

Think about scalability — moving from JSON to a database-backed phonebook.
