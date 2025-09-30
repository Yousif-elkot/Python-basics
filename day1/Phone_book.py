#!/usr/bin/env python3
"""
Phone Book CLI Application
A simple command-line interface for managing contacts.

Features:
- Add new contacts
- Search for contacts by name
- Delete existing contacts
- List all contacts
- Data persistence (saves to contacts.json)
- Error handling and input validation

Author: Yousif Elkattawy
Date: September 30, 2025
"""

import json
import os
import sys
from typing import Dict, Optional

# Save contacts to a JSON file
def save_contacts():
    with open("my_contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved!")

# Load contacts from the JSON file
def load_contacts():
    try:
        with open("my_contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist
    

# A simple dictionary to store contacts
print("Welcome to My Phone Book!")

contacts = {}
contacts = load_contacts()
print(f"loaded {len(contacts)} contacts")

# This loop keeps the program running
while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    """input handling for contact management"""
    if choice == "1":
        name = input("Enter contact name: ")
        # Check if name is empty
        if name.strip() == "":
            print("Name cannot be empty. Please try again.")
        else:
            phone = input("Enter contact phone number: ")
            # Check if phone number is empty
            if phone.strip() == "":
                print("Phone number cannot be empty. Please try again.")
            else:
                contacts[name] = phone
                print(f"Contact {name} added with phone number {phone}.")
    # Search for a contact
    elif choice == "2":
        search_name = input("Enter the name to search: ")

        if search_name in contacts:
            print(f"Found: {search_name} -> {contacts[search_name]}")
        else:
            print(f"Contact {search_name} not found.")   

    # Delete a contact  
    elif choice == "3":
        del_name = input("Enter the name to delete: ")

        if del_name in contacts:
            #show what we are deleting
            print(f"Deleting: {del_name} -> {contacts[del_name]}")

            #ask for confirmation
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                del contacts[del_name]
                print(f"Contact {del_name} deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Contact {del_name} not found.")

    # Show all contacts        
    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n--- Your Contacts ---")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
            print("---------------------")
    #exit the program
    elif choice == "5":
        #save contacts before exiting
        save_contacts()
        print("Goodbye!")
        break # Exit the loop and end the program
    else:
        print("Invalid choice. Please try again.")

