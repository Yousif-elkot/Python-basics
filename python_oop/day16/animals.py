"""
Animal Hierarchy - Day 16 Python Implementation
Demonstrating inheritance and polymorphism
"""
from typing import List


class Animal:
    """Base class for all animals"""
    
    def __init__(self, name: str, age: int):
        # TODO: Initialize attributes
        pass
    
    def make_sound(self) -> None:
        """Generic sound (to be overridden)"""
        # TODO: Print generic sound
        pass
    
    def sleep(self) -> None:
        """All animals sleep"""
        # TODO: Print sleep message
        pass
    
    def display_info(self) -> None:
        """Display animal information"""
        # TODO: Print name and age
        pass


class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name: str, age: int, breed: str):
        # TODO: Call parent constructor
        # TODO: Initialize breed
        pass
    
    def make_sound(self) -> None:
        """Override parent method"""
        # TODO: Print "Woof! Woof!"
        pass
    
    def fetch(self) -> None:
        """Dog-specific behavior"""
        # TODO: Print fetching message
        pass
    
    def display_info(self) -> None:
        """Extend parent method"""
        # TODO: Call parent version
        # TODO: Add breed info
        pass


class Cat(Animal):
    """Cat class for demonstrating polymorphism"""
    
    def __init__(self, name: str, age: int, indoor: bool = True):
        # TODO: Implement
        pass
    
    def make_sound(self) -> None:
        # TODO: Print "Meow!"
        pass


def demonstrate_polymorphism(animals: List[Animal]) -> None:
    """Demonstrate polymorphic behavior"""
    print("\n=== Demonstrating Polymorphism ===")
    # TODO: Loop through animals
    # Call make_sound and sleep for each
    pass


if __name__ == "__main__":
    # TODO: Create animal instances
    # TODO: Demonstrate polymorphism
    pass
