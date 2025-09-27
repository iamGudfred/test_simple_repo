#!/usr/bin/env python3
"""
Simple Calculator - Clean Test Application
Perfect for testing GitHub-to-EXE converter
No network requests, file operations, or dynamic imports
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return round(a / b, 4)

def power(a, b):
    """Raise a to the power of b"""
    if a < 0 and b != int(b):
        return "Error: Cannot raise negative number to non-integer power"
    return round(a ** b, 4)

def square_root(a):
    """Calculate square root"""
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    return round(a ** 0.5, 4)

def display_menu():
    """Display calculator menu"""
    print("\n=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("0. Exit")
    print("========================")

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            value = input(prompt).strip()
            if value.lower() == 'q':
                return None
            num = float(value)
            if abs(num) > 1e308:
                print("Number too large!")
                continue
            return num
        except ValueError:
            print("Please enter a valid number or 'q' to cancel!")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def main():
    """Main calculator function"""
    print("Welcome to Simple Calculator!")
    print("Built and tested with GitHub-to-EXE Converter")

    operations = {
        '1': (add, " + ", "Enter first number: ", "Enter second number: "),
        '2': (subtract, " - ", "Enter first number: ", "Enter second number: "),
        '3': (multiply, " × ", "Enter first number: ", "Enter second number: "),
        '4': (divide, " ÷ ", "Enter first number: ", "Enter second number: "),
        '5': (power, " ^ ", "Enter base number: ", "Enter exponent: "),
        '6': (square_root, "√", "Enter number: ", None)
    }

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (0-6): ").strip()
            if choice == '0':
                print("Thank you for using Simple Calculator!")
                break

            if choice not in operations:
                print("Invalid choice! Please select 0-6.")
                input("\nPress Enter to continue...")
                continue

            func, symbol, prompt1, prompt2 = operations[choice]
            a = get_number(prompt1)
            if a is None:
                print("Operation cancelled.")
                input("\nPress Enter to continue...")
                continue

            if prompt2:  # Operations requiring two inputs
                b = get_number(prompt2)
                if b is None:
                    print("Operation cancelled.")
                    input("\nPress Enter to continue...")
                    continue
                result = func(a, b)
                print(f"Result: {a} {symbol} {b} = {result}")
            else:  # Square root
                result = func(a)
                print(f"Result: {symbol}{a} = {result}")

            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
