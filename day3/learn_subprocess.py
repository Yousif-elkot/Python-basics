"""
System Monitor - Learning subprocess module
Step 1: Understanding how Python runs bash commands
"""

from pydoc import text
import subprocess

# ============================================================================
# LESSON 1: Running Simple Commands
# ============================================================================

def lesson1_basic_command():
    """Learn how to run a bash command and capture output."""
    print("="*60)
    print("LESSON 1: Basic Command Execution")
    print("="*60)
    
    # Run 'uptime' command
    # subprocess.run() executes the command and returns a CompletedProcess object
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    
    print("Command: uptime")
    print(f"Return code: {result.returncode}")  # 0 = success, non-zero = error
    print(f"Output:\n{result.stdout}")  # Standard output (what you see in terminal)
    print(f"Errors: {result.stderr}")   # Standard error (error messages)
    
    # Key concepts:
    # - ['uptime'] is a list: command and its arguments as separate items
    # - capture_output=True: Capture stdout and stderr
    # - text=True: Return string instead of bytes
    # - returncode: Exit code (0 = success)


def lesson2_command_with_arguments():
    """Learn how to pass arguments to commands."""
    print("\n" + "="*60)
    print("LESSON 2: Commands with Arguments")
    print("="*60)
    
    # Run 'free -m' (show memory in megabytes)
    result = subprocess.run(['free', '-m'], capture_output=True, text=True)
    
    print("Command: free -m")
    print(f"Output:\n{result.stdout}")
    
    # IMPORTANT: Arguments are separate list items!
    # CORRECT: ['free', '-m']
    # WRONG:   ['free -m']  # This treats "free -m" as one command name


def lesson3_parsing_output():
    """Learn how to parse command output."""
    print("\n" + "="*60)
    print("LESSON 3: Parsing Output")
    print("="*60)
    
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    output = result.stdout.strip()  # Remove leading/trailing whitespace
    
    print("Raw output:")
    print(output)
    
    # uptime output example:
    # " 20:30:15 up 5 days,  3:45,  2 users,  load average: 0.52, 0.58, 0.59"
    
    # Extract load average (the last 3 numbers)
    if 'load average:' in output:
        # Split by 'load average:' and take the second part
        load_part = output.split('load average:')[1].strip()
        # Split by commas to get individual values
        loads = [float(x.strip()) for x in load_part.split(',')]
        
        print(f"\nParsed load averages:")
        print(f"  1 min:  {loads[0]}")
        print(f"  5 min:  {loads[1]}")
        print(f"  15 min: {loads[2]}")


def lesson4_error_handling():
    """Learn how to handle command errors."""
    print("\n" + "="*60)
    print("LESSON 4: Error Handling")
    print("="*60)
    
    # Try running a command that doesn't exist
    try:
        result = subprocess.run(
            ['nonexistent_command'], 
            capture_output=True, 
            text=True,
            check=False  # Don't raise exception on non-zero return code
        )
        
        if result.returncode != 0:
            print("Command failed!")
            print(f"Return code: {result.returncode}")
            print(f"Error: {result.stderr}")
        else:
            print("Command succeeded!")
            print(f"Output: {result.stdout}")
    
    except FileNotFoundError:
        print("❌ Command not found!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def lesson5_practical_examples():
    """Practical examples of commands we'll use."""
    print("\n" + "="*60)
    print("LESSON 5: Practical Commands for System Monitor")
    print("="*60)
    
    commands = [
        (['free', '-m'], "Memory usage in MB"),
        (['df', '-h', '/'], "Disk usage in human-readable format"),
        (['uptime'], "System uptime and load average"),
        (['whoami'], "Current username"),
    ]
    
    for cmd, description in commands:
        print(f"\n{description}:")
        print(f"Command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)


# ============================================================================
# YOUR TURN: Practice Exercises
# ============================================================================

def exercise1_your_turn():
    """
    EXERCISE 1: Run 'df -h /' and print just the output.
    
    TODO: Fill in the code below.
    """
    print("\n" + "="*60)
    print("EXERCISE 1: Your Turn - Run 'df -h /'")
    print("="*60)
    
    # TODO: Use subprocess.run() to execute 'df -h /'
    # Hint: result = subprocess.run([...], capture_output=True, text=True)
    result = subprocess.run(['df','-h' ,'/'], capture_output=True, text=True)

    # TODO: Print the output
    # Hint: print(result.stdout)
    print(result.stdout)


def exercise2_parse_whoami():
    """
    EXERCISE 2: Run 'whoami' and extract just the username (no newline).
    
    TODO: Fill in the code below.
    """
    print("\n" + "="*60)
    print("EXERCISE 2: Parse Username")
    print("="*60)
    
    # TODO: Run 'whoami' command
    result = subprocess.run(['whoami'], capture_output=True, text=True)
    
    # TODO: Get the output and strip whitespace
    # Hint: username = result.stdout.strip()
    username = result.stdout.strip()

    # TODO: Print: "Current user: <username>"
    print(f"Current user: {username}")
    


# ============================================================================
# Run all lessons
# ============================================================================

if __name__ == "__main__":
    print("\n🎓 Learning subprocess Module - Python + Bash Integration\n")
    
    lesson1_basic_command()
    lesson2_command_with_arguments()
    lesson3_parsing_output()
    lesson4_error_handling()
    lesson5_practical_examples()
    
    # Now it's your turn!
    print("\n\n" + "="*60)
    print("🎯 YOUR EXERCISES:")
    print("="*60)
    print("\nEdit this file and complete exercise1_your_turn() and exercise2_parse_whoami()")
    print("Then run this file again to see your results!\n")
    
    # Uncomment these when you're ready:
    exercise1_your_turn()
    exercise2_parse_whoami()
