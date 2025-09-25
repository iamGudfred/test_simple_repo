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
      return a / b

  def power(a, b):
      """Raise a to the power of b"""
      return a ** b

  def square_root(a):
      """Calculate square root"""
      if a < 0:
          return "Error: Cannot calculate square root of negative number"
      return a ** 0.5

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
              return float(input(prompt))
          except ValueError:
              print("Please enter a valid number!")

  def main():
      """Main calculator function"""
      print("Welcome to Simple Calculator!")
      print("Built and tested with GitHub-to-EXE Converter")

      while True:
          display_menu()

          try:
              choice = input("Enter your choice (0-6): ").strip()
          except KeyboardInterrupt:
              print("\nGoodbye!")
              break

          if choice == '0':
              print("Thank you for using Simple Calculator!")
              break

          elif choice == '1':
              a = get_number("Enter first number: ")
              b = get_number("Enter second number: ")
              result = add(a, b)
              print(f"Result: {a} + {b} = {result}")

          elif choice == '2':
              a = get_number("Enter first number: ")
              b = get_number("Enter second number: ")
              result = subtract(a, b)
              print(f"Result: {a} - {b} = {result}")

          elif choice == '3':
              a = get_number("Enter first number: ")
              b = get_number("Enter second number: ")
              result = multiply(a, b)
              print(f"Result: {a} × {b} = {result}")

          elif choice == '4':
              a = get_number("Enter first number: ")
              b = get_number("Enter second number: ")
              result = divide(a, b)
              print(f"Result: {a} ÷ {b} = {result}")

          elif choice == '5':
              a = get_number("Enter base number: ")
              b = get_number("Enter exponent: ")
              result = power(a, b)
              print(f"Result: {a} ^ {b} = {result}")

          elif choice == '6':
              a = get_number("Enter number: ")
              result = square_root(a)
              print(f"Result: √{a} = {result}")

          else:
              print("Invalid choice! Please select 0-6.")

          input("\nPress Enter to continue...")

  if __name__ == "__main__":
      main()
