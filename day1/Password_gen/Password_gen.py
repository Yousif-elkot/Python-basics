#!/usr/bin/env python3
"""
Password Generator - Secure CLI Password Generation Tool

A professional command-line password generator with customizable security options.
Supports various character sets, length customization, and security features.

Author: [Your Name]
Date: September 30, 2025
Version: 1.0
"""

import random
import string
import argparse
import sys

def character_set(use_lowercase=True, use_uppercase=True, 
                  use_digits=True, use_symbols=True, 
                  exclude_ambiguous=False):
    """
    Build a character set based on user preferences.
    
    Args:
        use_lowercase (bool): Include lowercase letters (a-z). Default: True
        use_uppercase (bool): Include uppercase letters (A-Z). Default: True
        use_digits (bool): Include numeric digits (0-9). Default: True
        use_symbols (bool): Include punctuation symbols. Default: True
        exclude_ambiguous (bool): Exclude visually similar characters (Il1O0). Default: False
    
    Returns:
        str: A string containing all allowed characters for password generation
        
    Example:
        >>> charset = character_set(use_symbols=False, exclude_ambiguous=True)
        >>> 'I' in charset
        False
        >>> '!' in charset
        False
    """
    char_set = ""
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation  
    if exclude_ambiguous:
        ambiguous_chars = 'Il1O0'
        char_set = ''.join(c for c in char_set if c not in ambiguous_chars)
    return char_set

def generate_password(length=12, character_set="", ensure_variety=True):
    """
    Generate a cryptographically secure password with specified criteria.
    
    Args:
        length (int): Desired password length. Must be >= 4 if ensure_variety=True. Default: 12
        character_set (str): String of allowed characters for password generation
        ensure_variety (bool): Guarantee at least one character from each enabled type. Default: True
    
    Returns:
        str: A randomly generated password meeting the specified criteria
        
    Raises:
        ValueError: If character_set is empty or length is too short for variety requirements
        
    Example:
        >>> charset = character_set(use_symbols=False)
        >>> password = generate_password(length=16, character_set=charset)
        >>> len(password)
        16
        >>> any(c in string.punctuation for c in password)
        False
    """
    if not character_set:
        raise ValueError("Character set cannot be empty.")
    
    if length < 4 and ensure_variety:
        raise ValueError("Length must be at least 4 to ensure variety.")

    Password = []
    if ensure_variety:
        # Instead of checking all categories, build categories from the actual character_set
        required_chars = []
        if any(c in character_set for c in string.ascii_lowercase):
            required_chars.append(random.choice([c for c in string.ascii_lowercase if c in character_set]))
        if any(c in character_set for c in string.ascii_uppercase):
            required_chars.append(random.choice([c for c in string.ascii_uppercase if c in character_set]))
        if any(c in character_set for c in string.digits):
            required_chars.append(random.choice([c for c in string.digits if c in character_set]))
        if any(c in character_set for c in string.punctuation):
            required_chars.append(random.choice([c for c in string.punctuation if c in character_set]))
        
        Password.extend(required_chars)
        length -= len(Password)    

    # Fill the remaining length with random choices from the character set
    Password.extend(random.choices(character_set, k=length))
    random.shuffle(Password)
    return ''.join(Password)

def parse_arguments():
    """
    Parse and validate command-line arguments for the password generator.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments with the following attributes:
            - length (int): Password length (default: 12)
            - count (int): Number of passwords to generate (default: 1)
            - no_lowercase (bool): Exclude lowercase letters
            - no_uppercase (bool): Exclude uppercase letters
            - no_digits (bool): Exclude digits
            - no_symbols (bool): Exclude symbols
            - no_ambiguous (bool): Exclude ambiguous characters
            - no_variety (bool): Disable variety enforcement
    
    Example:
        $ python Password_gen.py -l 16 -c 3 --no-symbols
        Creates arguments for 3 passwords, 16 characters each, no symbols
    """
    parser = argparse.ArgumentParser(description='Generate secure passwords')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords to generate')
    parser.add_argument('--no-lowercase', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-uppercase', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    parser.add_argument('--no-ambiguous', action='store_true', help='Exclude ambiguous characters (Il1O0)')
    parser.add_argument('--no-variety', action='store_true', help='Do not ensure variety of character types')
    return parser.parse_args()

def get_password_strength(password):
    """
    Analyze password strength based on character diversity and length.
    
    Scoring criteria:
    - +1 point for each character type present (lowercase, uppercase, digits, symbols)
    - +1 point for length >= 12 characters
    - +1 point for length >= 16 characters
    
    Args:
        password (str): The password to analyze
        
    Returns:
        str: Password strength rating from "Very Weak" to "Excellent"
        
    Example:
        >>> get_password_strength("Abc123!@#xyz")
        'Very Strong'
        >>> get_password_strength("abc")
        'Very Weak'
    """
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Excellent"]
    return strength[min(score, 5)]

def main():
    """
    Main program entry point - orchestrates password generation workflow.
    
    Process:
    1. Parse command-line arguments
    2. Convert exclusion flags to inclusion settings
    3. Build character set based on user preferences
    4. Validate configuration (non-empty charset, adequate length)
    5. Generate requested number of passwords
    6. Display results with formatting and strength analysis
    
    Exits with status code 1 on configuration errors or generation failures.
    """
    # 1. Parse command line arguments
    args = parse_arguments()

    # 2. Convert --no-* flags to positive flags for character_set()
    use_lowercase = not args.no_lowercase
    use_uppercase = not args.no_uppercase
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols
    exclude_ambiguous = args.no_ambiguous
    ensure_variety = not args.no_variety

    # 3. Build the character set
    char_set = character_set(use_lowercase, use_uppercase, 
                             use_digits, use_symbols, 
                             exclude_ambiguous)

    # 4. Validate inputs (length, character set not empty)
    if not char_set:
        print("Error: Character set is empty. Enable at least one character type.")
        sys.exit(1)
    
    if args.length < 4 and ensure_variety:
        print("Error: Length must be at least 4 to ensure variety.")
        sys.exit(1)

    # 5. Generate the requested number of passwords
    passwords = []
    for _ in range(args.count):
        try:
            pwd = generate_password(length=args.length, 
                                    character_set=char_set, 
                                    ensure_variety=ensure_variety)
            passwords.append(pwd)
        except ValueError as ve:
            print(f"Error: {ve}")
            sys.exit(1)

    # 6. Display results nicely
    print(f"\nGenerated {args.count} password(s) with length {args.length}:")
    print(f"Character types: {'Lowercase ' if use_lowercase else ''}{'Uppercase ' if use_uppercase else ''}{'Digits ' if use_digits else ''}{'Symbols ' if use_symbols else ''}")
    if exclude_ambiguous:
        print("(Ambiguous characters excluded)")
    print(f"Password strength: {get_password_strength(pwd)}")
    print("-" * 40)
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}: {pwd}")

if __name__ == "__main__":
    main()