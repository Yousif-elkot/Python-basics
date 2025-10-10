import json
import os
from datetime import datetime
from typing import List, Dict, Optional


# DATA STRUCTURE DESIGN
# =====================
# Main data structure: LIST (dynamic array) containing DICTIONARIES
# Each todo is a dictionary with structured fields:
# {
#     "id": int,           # Unique identifier
#     "text": str,         # Todo description  
#     "priority": str,     # "high", "medium", "low"
#     "status": str,       # "pending", "completed"
#     "created_date": str, # ISO format timestamp
#     "category": str      # Category for organization
# }


def create_todo(text: str, priority: str = "medium", category: str = "general") -> Dict:
    """Create a new todo item."""
    return {
        "id": 0, # Will be set when added to array
        "text": text,
        "priority": priority.lower(),
        "status": "pending",
        "created_date": datetime.now().isoformat(),
        "category": category
    }

#Display menu options
def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("📝 SMART TODO LIST MENU")
    print("=" * 40)
    print("1. ➕ Add Todo")
    print("2. 📋 Display All Todos")
    print("3. 🔍 Search Todos")
    print("4. 📊 Sort Todos")
    print("5. ❌ Remove Todo")
    print("6. ✅ Mark Complete")
    print("7. 💾 Save Todos")
    print("8. 🚪 Exit")

def add_todo(todos: list[Dict]) -> None:
    """add a new todo item to the array
    
    ARRAY OPERATION: Insertion
    - Appends to end of list (O(1) amortized complexity)
    - Demonstrates dynamic array growth
    - Auto-assigns ID based on array length
    """
    text = input("Enter todo description: ").strip()
    if not text:
        print("❌ Description cannot be empty!")
        return

    priority = input("Enter priority (high/medium/low) (default: medium): ").strip() or "medium"
    if priority not in ["high", "medium", "low"]:
        print("❌ Invalid priority! Using 'medium'")
        priority = "medium"
 
    category = input("Enter category (default: general): ").strip() or "general"

    new_todo = create_todo(text, priority, category)
    new_todo["id"] = len(todos) + 1  # Assign ID based on current length
    todos.append(new_todo)
    # this is O(1) amortized complexity

def display_todos(todos: list[Dict]) -> None:
     
    """
    Display all todos in the array.
     
    ARRAY OPERATION: TRAVERSAL
    - Iterates through entire array (O(n) complexity)
    - Demonstrates array indexing and access patterns
    """
    if not todos:
        print("No todos to display.")
        return
    print(f"Total todos: {len(todos)}")
    print()

    # ARRAY OPERATION: Iterate through all elements
    for i, todo in enumerate(todos):
        status_emoji = "✅" if todo["status"] == "completed" else "⏳"
        priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(todo["priority"], "⚪")
        print(f"{status_emoji} Todo #{todo['id']} {priority_emoji}")
        print(f"   📝 {todo['text']}")
        print(f"Status: {todo['status']}")
        print(f"   🎯 Priority: {todo['priority']}")
        print(f"Created Date: {todo['created_date']}")
        print(f"Category: {todo['category']}")
        print("-" * 20)

def remove_todo(todos: list[Dict]) -> None:
    """Remove a todo item by ID.
    
    ARRAY OPERATION: Deletion
    - Searches for item by ID (O(n) complexity)
    - Removes item and shifts subsequent elements (O(n) complexity)
    """
    if not todos:
        print("No todos to remove.")
        return
    
    display_todos(todos)

    try:
        todo_id = int(input("Enter the ID of the todo to remove: "))
    except ValueError:
            print("Invalid ID. Please enter a number.")
            return
    
    # ARRAY OPERATION: Search for item by ID
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            # ARRAY OPERATION: Remove item and shift elements
            removed_todo = todos.pop(i)
            print(f"Removed todo: {removed_todo['text']}")
            return

    print(f"Todo with ID {todo_id} not found.")

def mark_todo_completed(todos: list[Dict]) -> None:
    """Mark a todo item as completed by ID.
    
    ARRAY OPERATION: Search and Update
    - Searches for item by ID (O(n) complexity)
    - Updates status field (O(1) complexity)
    """
    if not todos:
        print("No todos to mark as completed.")
        return
    
    #show only pending todos
    pending_todos = [todo for todo in todos if todo["status"] == "pending"]
    if not pending_todos:
        print("No pending todos to mark as completed.")
        return
    
    print("Pending Todos:")
    for todo in pending_todos:
        print(f"ID: {todo['id']}, Description: {todo['text']}")
    
    try:
        todo_id = int(input("Enter the ID of the todo to mark as completed: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    # ARRAY OPERATION: linear search and update
    for todo in todos:
        if todo["id"] == todo_id:
            if todo["status"] == "pending":
                todo["status"] = "completed"
                print(f"Marked todo with ID {todo_id} as completed.")
            else:
                print(f"Todo with ID {todo_id} is already completed.")
            return
    

# SEARCH ALGROTHIMS
def search_todos(todos: List[Dict]) -> None:
    """
    Search todos using various linear search algorithms.
    
    ALGORITHM: LINEAR SEARCH
    - Searches through array sequentially
    - O(n) time complexity
    - Multiple search criteria supported
    """
    print("\n🔍 SEARCH TODOS")
    print("-" * 20)
    
    if not todos:
        print("📭 No todos to search!")
        return
    
    print("Search options:")
    print("1. Search by text (contains)")
    print("2. Search by priority")
    print("3. Search by status")
    print("4. Search by category")
    
    choice = input("Choose search type (1-4): ").strip()
    
    if choice == "1":
        search_by_text(todos)
    elif choice == "2":
        search_by_priority(todos)
    elif choice == "3":
        search_by_status(todos)
    elif choice == "4":
        search_by_category(todos)
    else:
        print("❌ Invalid search option!")

def search_by_text(todos: List[Dict]) -> None:
    """
    LINEAR SEARCH ALGORITHM: Search by text content.
    Demonstrates substring matching and case-insensitive search.
    """
    search_term = input("Enter text to search for: ").strip().lower()
    if not search_term:
        print("❌ Search term cannot be empty!")
        return
    
    found_todos = []

    #Linear search: O(n) complexity
    for todo in todos:
        if search_term in todo["text"].lower():
            found_todos.append(todo)
    
    display_search_results(found_todos,f"Text contains '{search_term}'")

def search_by_priority(todos: List[Dict]) -> None:
    """
    LINEAR SEARCH ALGORITHM: Search by exact priority match.
    """
    priority = input("Enter priority to search for (high, medium, low): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        print("❌ Invalid priority!")
        return
    
    found_todos = []

    #Linear search: O(n) complexity
    for todo in todos:
        if todo["priority"] == priority:
            found_todos.append(todo)

    display_search_results(found_todos,f"Priority is '{priority}'")

def search_by_status(todos: List[Dict]) -> None:
    """
    LINEAR SEARCH ALGORITHM: Search by exact status match.
    """
    status = input("Enter status to search for (pending, completed): ").strip().lower()
    if status not in ["pending", "completed"]:
        print("❌ Invalid status!")
        return
    
    found_todos = []

    #Linear search: O(n) complexity
    for todo in todos:
        if todo["status"] == status:
            found_todos.append(todo)

    display_search_results(found_todos,f"Status is '{status}'")

def search_by_category(todos: List[Dict]) -> None:
    """
    LINEAR SEARCH ALGORITHM: Search by exact category match.
    """
    category = input("Enter category to search for: ").strip().lower()
    if not category:
        print("❌ Category cannot be empty!")
        return
    
    found_todos = []

    #Linear search: O(n) complexity
    for todo in todos:
        if todo["category"].lower() == category:
            found_todos.append(todo)

    display_search_results(found_todos,f"Category is '{category}'")

def display_search_results(found_todos: List[Dict], criteria: str) -> None:
    """Display search results."""
    if not found_todos:
        print(f"🔍 No todos found matching criteria: {criteria}")
        return
    
    print(f"🔍 Found {len(found_todos)} todos matching criteria: {criteria}")
    print("-" * 20)
    for todo in found_todos:
        status_emoji = "✅" if todo["status"] == "completed" else "⏳"
        priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(todo["priority"], "⚪")
        print(f"{status_emoji} Todo #{todo['id']} {priority_emoji}")
        print(f"   📝 {todo['text']}")
        print(f"Status: {todo['status']}")
        print(f"   🎯 Priority: {todo['priority']}")
        print(f"Created Date: {todo['created_date']}")
        print(f"Category: {todo['category']}")
        print("-" * 20)


# SORTING ALGORITHMS
def sort_todos(todos: List[Dict]) -> None:
    """
    Sort todos using various algorithms and criteria.
    
    ALGORITHMS DEMONSTRATED:
    - Python's built-in sort (Timsort - hybrid merge/insertion sort)
    - Custom comparison functions
    - Stable sorting (maintains relative order of equal elements)
    """
    print("\n📊 SORT TODOS")
    print("-" * 20)
    
    if not todos:
        print("📭 No todos to sort!")
        return
    
    print("Sort options:")
    print("1. Sort by priority (high → medium → low)")
    print("2. Sort by status (pending → completed)")
    print("3. Sort by creation date (newest → oldest)")
    print("4. Sort by text (alphabetical)")
    print("5. Sort by category")

    choice = input("Choose sort type (1-5): ").strip()

    if choice == "1":
        sort_by_priority(todos)
    elif choice == "2":
        sort_by_status(todos)
    elif choice == "3":
        sort_by_date(todos)
    elif choice == "4":
        sort_by_text(todos)
    elif choice == "5":
        sort_by_category(todos)
    else:
        print("❌ Invalid sort option!")

def sort_by_priority(todos: List[Dict]) -> None:
    """
    SORTING ALGORITHM: Sort by priority using custom key function.
    Uses Python's Timsort algorithm with O(n log n) complexity.
    """
    priority_order = {"high": 1, "medium": 2, "low": 3}

    #SORT ALGORITHM: Timesort with custom key function
    todos.sort(key=lambda todo: priority_order.get(todo["priority"], 4))

    print("✅ Todos sorted by priority (high → medium → low)")
    display_todos(todos)

def sort_by_status(todos: List[Dict] ) -> None:
    """
    SORTING ALGORITHM: Sort by status (pending first, then completed).
    """
    #SORT ALGORITHM: Sort with pending todos first
    todos.sort(key=lambda todo : todo["status"] == "completed")

    print("✅ Todos sorted by status (pending → completed)")
    display_todos(todos)

def sort_by_date(todos: List[Dict]) -> None:
    """
    SORTING ALGORITHM: Sort by creation date (newest first).
    """
    #SORT ALGORITHM: Sort by ISO date string (newest first)
    todos.sort(key=lambda todo: todo["created_date"], reverse=True)

    print("✅ Todos sorted by creation date (newest → oldest)")
    display_todos(todos)

def sort_by_text(todos: List[Dict]) -> None:
    """
    SORTING ALGORITHM: Alphabetical sort (case-insensitive).
    """
    # SORT ALGORITHM: Case-insensitive alphabetical sort
    todos.sort(key=lambda todo: todo["text"].lower())

    print("✅ Todos sorted alphabetically")
    display_todos(todos)

def sort_by_category(todos: List[Dict]) -> None:
    """
    SORTING ALGORITHM: Sort by category, then by priority within each category.
    Demonstrates stable sorting with multiple criteria.
    """
    priority_order = {"high": 1, "medium": 2, "low": 3}

    # SORT ALGORITHM: Multi-Level sort (category first, then priority)
    todos.sort(key=lambda todo: (
        todo["category"].lower(),
        priority_order.get(todo["priority"], 4)
    ))

    print("✅ Todos sorted by category, then priority")
    display_todos(todos)


# DATA PERSISTENCE
# ================

def save_todos(todos: List[Dict]) -> None:
    """
    Save todos to JSON file for persistence.
    
    ARRAY OPERATION: Serialization
    - Converts entire array to JSON format
    - File I/O operations
    """
    filename = "todos.json"
    try:
        with open(filename, 'w') as file:
            json.dump(todos,file,indent = 2)
    except Exception as e:
        print(f"❌ Error saving todos: {e}")

def load_todos() -> List[Dict]:
    """
    Load todos from JSON file.
    
    ARRAY OPERATION: Deserialization
    - Loads array from file
    - Handles file not found gracefully
    """
    filename = "todos.json"

    if not os.path.exists(filename):
        print("📭 No saved todos found. Starting with empty list.")
        return []
    try:
        with open(filename, 'r') as file:
            todos = json.load(file)
            print(f"📂 Loaded {len(todos)} saved todo(s)")
            return todos
    except Exception as e:
        print(f"❌ Error loading todos: {e}")
        return []
    
def main():
    """Main entry point for the Smart Todo List application."""
    print("🚀 Welcome to Smart Todo List!")
    print("=" * 40)
    print("📚 Learning Focus: Arrays, Lists & Search Algorithms")
    print("💡 Day 2 Project - Data Structures & Algorithms")
    
    # Initialize empty todo list (our main data structure - an array/list)
    todos = []
    
    # Load existing todos if available
    todos = load_todos()

    while True:
        display_menu()
        choice = input("\n Enter your choice(1-8): ").strip()

        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            display_todos(todos)
        elif choice == '3':
            search_todos(todos)
        elif choice == '4':
            sort_todos(todos)
        elif choice == '5':
            remove_todo(todos)
        elif choice == '6':
            mark_todo_completed(todos)
        elif choice == '7':
            save_todos(todos)
            print("✅ Todos saved successfully!")
        elif choice == '8':
            save_todos(todos)
            print("\n👋 Goodbye! Your todos have been saved.")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


