"""
BankAccount class - Day 15 Python Implementation
TODO: Complete this implementation following the README.md
"""


class BankAccount:
    """Represents a bank account with basic operations"""
    
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        """
        Initialize a new bank account.
        
        Args:
            account_number: Unique account identifier
            owner: Account owner name
            initial_balance: Starting balance (default 0.0)
        """
        # TODO: Initialize private attributes
        pass
    
    @property
    def account_number(self) -> str:
        """Get account number (read-only)"""
        # TODO: Return account number
        pass
    
    @property
    def owner(self) -> str:
        """Get owner name"""
        # TODO: Return owner
        pass
    
    @owner.setter
    def owner(self, value: str) -> None:
        """Set owner name with validation"""
        # TODO: Set owner (validate not empty)
        pass
    
    @property
    def balance(self) -> float:
        """Get current balance (read-only)"""
        # TODO: Return balance
        pass
    
    def deposit(self, amount: float) -> None:
        """Deposit money into account"""
        # TODO: Add amount to balance if valid
        # Print confirmation
        pass
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account.
        
        Returns:
            True if successful, False otherwise
        """
        # TODO: Subtract amount if valid
        # Return success status
        pass
    
    def display_info(self) -> None:
        """Display account information"""
        # TODO: Print account details
        pass
    
    def __str__(self) -> str:
        """String representation"""
        # TODO: Return user-friendly string
        pass
    
    def __repr__(self) -> str:
        """Developer-friendly representation"""
        # TODO: Return detailed representation
        pass


# Testing
if __name__ == "__main__":
    # TODO: Create a BankAccount instance
    # Test deposit and withdraw
    # Display account info
    pass
