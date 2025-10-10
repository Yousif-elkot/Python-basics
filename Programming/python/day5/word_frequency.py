"""
Word Frequency Analyzer - Day 5 Project 2
==========================================

A CLI tool that analyzes text files and counts word frequencies.

Features:
- Count word frequencies in text files
- Filter common stop words ("the", "a", "an", etc.)
- Display top N most common words
- Export results to JSON or CSV
- Beautiful CLI with argparse

YOUR MISSION: Implement the core functions!
"""

import argparse
import json
import csv
import re
from collections import Counter
from pathlib import Path


# Stop words to filter out (common words with little meaning)
STOP_WORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
    'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that',
    'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
    'my', 'your', 'his', 'her', 'its', 'our', 'their'
}


def read_file(filepath):
    """
    TODO #1: Read text from a file
    
    Algorithm:
    1. Open the file with encoding='utf-8' to handle special characters
    2. Read all text: text = f.read()
    3. Return the text
    4. Handle FileNotFoundError - print error and return empty string
    
    Args:
        filepath (str): Path to the text file
        
    Returns:
        str: The file content, or empty string if error
        
    Hint: Use try/except for error handling
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' not found")
        return ""


def tokenize(text):
    """
    TODO #2: Convert text into a list of words
    
    Algorithm:
    1. Convert to lowercase: text = text.lower()
    2. Use regex to find all words: re.findall(r'\b[a-z]+\b', text)
       - \b = word boundary
       - [a-z]+ = one or more letters
       - This removes punctuation and numbers
    3. Return the list of words
    
    Args:
        text (str): The input text
        
    Returns:
        list: List of words (all lowercase, no punctuation)
        
    Example:
        tokenize("Hello, World! 123") → ["hello", "world"]
    """
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    return words

def remove_stop_words(words, use_stop_words=True):
    """
    TODO #3: Filter out common stop words
    
    Algorithm:
    1. If not use_stop_words, return words as-is
    2. Use list comprehension to filter:
       filtered = [word for word in words if word not in STOP_WORDS]
    3. Return filtered list
    
    Args:
        words (list): List of words
        use_stop_words (bool): Whether to filter stop words
        
    Returns:
        list: Filtered list of words
        
    Example:
        remove_stop_words(["the", "cat", "and", "dog"])
        → ["cat", "dog"]
    """
    if not use_stop_words:
        return words

    filtered = [word for word in words if word not in STOP_WORDS]
    return filtered


def count_frequencies(words):
    """
    TODO #4: Count word frequencies
    
    Algorithm:
    1. Use Counter from collections: counter = Counter(words)
    2. Return the Counter object
    
    Args:
        words (list): List of words
        
    Returns:
        Counter: Word frequency counter
        
    Example:
        count_frequencies(["cat", "dog", "cat"])
        → Counter({'cat': 2, 'dog': 1})
    """
    counter = Counter(words)
    return counter


def get_top_words(counter, n=10):
    """
    TODO #5: Get top N most common words
    
    Algorithm:
    1. Use counter.most_common(n) - returns list of (word, count) tuples
    2. Return the result
    
    Args:
        counter (Counter): Word frequency counter
        n (int): Number of top words to return
        
    Returns:
        list: List of (word, count) tuples
        
    Example:
        get_top_words(Counter({'cat': 5, 'dog': 3, 'bird': 1}), n=2)
        → [('cat', 5), ('dog', 3)]
    """
    return counter.most_common(n)


def display_results(top_words, total_words, unique_words):
    """
    Display results in a nice format.
    
    THIS ONE IS DONE FOR YOU! 🎉
    """
    print("\n" + "="*60)
    print("📊 WORD FREQUENCY ANALYSIS RESULTS")
    print("="*60)
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"\nTop {len(top_words)} most common words:")
    print("-"*60)
    
    # Find longest word for formatting
    max_word_len = max(len(word) for word, count in top_words) if top_words else 10
    
    for i, (word, count) in enumerate(top_words, 1):
        # Create a bar chart
        bar_length = int(count / top_words[0][1] * 40) if top_words else 0
        bar = "█" * bar_length
        
        print(f"{i:2d}. {word:<{max_word_len}} {count:>5} {bar}")
    
    print("="*60 + "\n")


def export_to_json(top_words, output_file):
    """
    TODO #6: Export results to JSON file
    
    Algorithm:
    1. Convert top_words to a dict: data = dict(top_words)
    2. Open file in write mode: with open(output_file, 'w') as f:
    3. Write JSON: json.dump(data, f, indent=2)
    4. Print success message
    5. Handle errors with try/except
    
    Args:
        top_words (list): List of (word, count) tuples
        output_file (str): Output file path
    """
    data = dict(top_words)
    try:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Results exported to JSON file: {output_file}")
    except Exception as e:
        print(f"❌ Error exporting to JSON: {e}")


def export_to_csv(top_words, output_file):
    """
    TODO #7: Export results to CSV file
    
    Algorithm:
    1. Open file in write mode: with open(output_file, 'w', newline='') as f:
    2. Create CSV writer: writer = csv.writer(f)
    3. Write header: writer.writerow(['Word', 'Count'])
    4. Write rows: writer.writerows(top_words)
    5. Print success message
    6. Handle errors with try/except
    
    Args:
        top_words (list): List of (word, count) tuples
        output_file (str): Output file path
    """
    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Word', 'Count'])
            writer.writerows(top_words)
        print(f"✅ Results exported to CSV file: {output_file}")
    except Exception as e:
        print(f"❌ Error exporting to CSV: {e}")


def analyze_file(filepath, top_n=10, filter_stop_words=True, export_format=None, output_file=None):
    """
    Main analysis function - orchestrates everything.
    
    THIS ONE IS DONE FOR YOU! 🎉
    It calls all your functions in the right order.
    """
    print(f"\n📖 Reading file: {filepath}")
    
    # Step 1: Read file
    text = read_file(filepath)
    if not text:
        return
    
    # Step 2: Tokenize
    print("🔤 Tokenizing text...")
    words = tokenize(text)
    
    # Step 3: Remove stop words (optional)
    if filter_stop_words:
        print("🚫 Filtering stop words...")
        words = remove_stop_words(words, use_stop_words=True)
    
    # Step 4: Count frequencies
    print("🔢 Counting word frequencies...")
    counter = count_frequencies(words)
    
    # Step 5: Get top N words
    top_words = get_top_words(counter, n=top_n)
    
    # Step 6: Display results
    total_words = len(words)
    unique_words = len(counter)
    display_results(top_words, total_words, unique_words)
    
    # Step 7: Export (optional)
    if export_format and output_file:
        if export_format == 'json':
            export_to_json(top_words, output_file)
        elif export_format == 'csv':
            export_to_csv(top_words, output_file)


def main():
    """
    Command-line interface using argparse.
    
    THIS ONE IS DONE FOR YOU! 🎉
    """
    parser = argparse.ArgumentParser(
        description='Analyze word frequencies in text files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s sample.txt
  %(prog)s sample.txt --top 20
  %(prog)s sample.txt --no-filter
  %(prog)s sample.txt --export json --output results.json
  %(prog)s sample.txt --export csv --output results.csv
        """
    )
    
    parser.add_argument(
        'file',
        help='Text file to analyze'
    )
    
    parser.add_argument(
        '--top', '-t',
        type=int,
        default=10,
        help='Number of top words to display (default: 10)'
    )
    
    parser.add_argument(
        '--no-filter',
        action='store_true',
        help='Don\'t filter stop words'
    )
    
    parser.add_argument(
        '--export',
        choices=['json', 'csv'],
        help='Export format (json or csv)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file path (required if --export is used)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.export and not args.output:
        parser.error("--output is required when --export is specified")
    
    # Run analysis
    analyze_file(
        filepath=args.file,
        top_n=args.top,
        filter_stop_words=not args.no_filter,
        export_format=args.export,
        output_file=args.output
    )


if __name__ == "__main__":
    main()
