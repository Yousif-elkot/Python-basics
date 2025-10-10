#!/usr/bin/env python3
"""
Day 1 — Unit Converter (improved)

Improvements:
- refactored conversion logic into small, testable functions
- input validation (retry on invalid numbers)
- interactive loop (do multiple conversions until user quits)
- graceful exit on Ctrl+C / EOF and 'q' command to quit
- clearer prompts and output formatting

Usage:
    python day1/unit_converter.py
"""
from typing import NoReturn


 # Conversion functions

def km_to_miles(km: float) -> float:
    """Return miles for given kilometers """ 
    return km * 0.621371

def miles_to_km(mi:float) -> float:
    """Return kilometers as miles """
    return mi /0.621371 

def c_to_f(c:float) -> float:
    """Convert Celsius to Fahrenheit """
    return (c * 9/5) +32

def f_to_c(f:float) -> float:
    """Convert Fahrenheit to Celsius """
    return (f - 32) * 5/9


# Input helpers

def ask_float(prompt: str) -> float:
    """
    prompt user until a valid float is entered
    user can type 'q' (or 'quit'/'exit') to raise keyboard interrupt which is handled by the main loop
    """

    while True:
        s = input(prompt).strip()
        if s.lower() in ("q", "quit" , "exit"):
            #start a keyboard interrupt to be handled by caller (clean exit)
            raise KeyboardInterrupt
        try:
            return float(s)
        except ValueError:
            print("→ Please enter a valid number (or type 'q' to quit).")


def get_choice() -> str:
    """Prompt the menu choice and return normal string """
    return input("Choose and option (1-4) or 'q' to quit: ").strip().lower()


# UI/menu

def print_menu() -> None:
    """Show the available options"""
    print("📏 Unit Converter")
    print("1. Kilometers → Miles")
    print("2. Miles → Kilometers")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("Type 'q' to quit")


def handle_choice(choice: str) -> None:
    """Execute action based on choice"""
    if choice == "1":
        km= ask_float("Enter Kilometers: ")
        miles = km_to_miles(km)
        print(f"{km} km = {miles:.4f} miles")
    elif choice == "2":
        mi = ask_float("Enter miles: ")
        km = miles_to_km(mi)
        print(f"{mi} miles = {km:.4f} km")

    elif choice == "3":
        c = ask_float("Enter Celsius: ")
        f = c_to_f(c)
        print(f"{c}°C = {f:.2f}°F")

    elif choice == "4":
        f = ask_float("Enter Fahrenheit: ")
        c = f_to_c(f)
        print(f"{f}°F = {c:.2f}°C")

    else:
        print("❌ Invalid choice — please pick 1,2,3,4 or 'q'.")


# Main program loop


def main():
    """Main loop, Repeats until user quits"""
    print("Welcome — Unit Converter (Day 1 improved)")
    try:
        while True:
            print_menu()
            choice = get_choice()
            if choice in ("q" , "quit" , "exit"):
                print("Goodbye!")
                break
            handle_choice(choice)
    except KeyboardInterrupt:
        # When user types 'q' or Ctrl+C
        print("\nExiting... Goodbye!")
    except EOFError:
        # in case of Ctrl+D or stdin closed
        print("\nInput closed. Exiting...")
# Run program if this file is executed directly
if __name__ == "__main__":
    main()
