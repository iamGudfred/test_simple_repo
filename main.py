  #!/usr/bin/env python3
  """
  Simple GUI Calculator - Clean Test Application
  Perfect for testing GitHub-to-EXE converter with windowed mode
  No console input needed - pure GUI interface
  """

  import tkinter as tk
  from tkinter import messagebox
  import math

  class Calculator:
      def __init__(self, root):
          self.root = root
          self.root.title("Simple GUI Calculator")
          self.root.geometry("350x450")
          self.root.resizable(False, False)

          # Configure style
          self.root.configure(bg='#f0f0f0')

          self.create_widgets()
          self.reset_calculator()

      def create_widgets(self):
          # Title
          title_label = tk.Label(
              self.root,
              text="GitHub-to-EXE Calculator",
              font=("Arial", 16, "bold"),
              bg='#f0f0f0',
              fg='#333'
          )
          title_label.pack(pady=10)

          # Display
          self.display_var = tk.StringVar()
          self.display_var.set("0")

          display = tk.Entry(
              self.root,
              textvariable=self.display_var,
              font=("Arial", 18),
              justify='right',
              state='readonly',
              width=20
          )
          display.pack(pady=10, padx=20, fill='x')

          # Button frame
          button_frame = tk.Frame(self.root, bg='#f0f0f0')
          button_frame.pack(pady=10)

          # Button layout
          buttons = [
              ['C', '±', '%', '÷'],
              ['7', '8', '9', '×'],
              ['4', '5', '6', '-'],
              ['1', '2', '3', '+'],
              ['0', '.', '=', '√']
          ]

          for i, row in enumerate(buttons):
              for j, btn_text in enumerate(row):
                  self.create_button(button_frame, btn_text, i, j)

      def create_button(self, parent, text, row, col):
          # Button colors
          if text == '=':
              bg_color = '#4CAF50'
              fg_color = 'white'
          elif text in ['C', '±', '%', '÷', '×', '-', '+', '√']:
              bg_color = '#2196F3'
              fg_color = 'white'
          else:
              bg_color = '#e0e0e0'
              fg_color = 'black'

          button = tk.Button(
              parent,
              text=text,
              font=("Arial", 14, "bold"),
              width=6,
              height=2,
              bg=bg_color,
              fg=fg_color,
              command=lambda: self.button_click(text)
          )
          button.grid(row=row, column=col, padx=3, pady=3)

      def reset_calculator(self):
          self.first_number = None
          self.operation = None
          self.waiting_for_operand = False

      def button_click(self, value):
          if value == 'C':
              self.reset_calculator()
              self.display_var.set("0")
          elif value == '=':
              self.calculate()
          elif value == '±':
              self.toggle_sign()
          elif value == '%':
              self.percentage()
          elif value == '√':
              self.square_root()
          elif value in ['÷', '×', '-', '+']:
              self.handle_operator(value)
          else:
              self.handle_number(value)

      def handle_number(self, num):
          current = self.display_var.get()

          if self.waiting_for_operand:
              if num == '.':
                  self.display_var.set("0.")
              else:
                  self.display_var.set(num)
              self.waiting_for_operand = False
          else:
              if num == '.' and '.' in current:
                  return  # Prevent multiple decimals

              if current == "0":
                  if num == '.':
                      self.display_var.set("0.")
                  else:
                      self.display_var.set(num)
              else:
                  self.display_var.set(current + num)

      def handle_operator(self, op):
          current_value = float(self.display_var.get())

          if self.first_number is None:
              self.first_number = current_value
          elif self.operation and not self.waiting_for_operand:
              self.calculate()
              current_value = float(self.display_var.get())
              self.first_number = current_value

          self.operation = op
          self.waiting_for_operand = True

      def calculate(self):
          if self.operation is None or self.first_number is None:
              return

          try:
              second_number = float(self.display_var.get())
              result = 0

              # Safe calculation - no dynamic code execution
              if self.operation == '+':
                  result = self.first_number + second_number
              elif self.operation == '-':
                  result = self.first_number - second_number
              elif self.operation == '×':
                  result = self.first_number * second_number
              elif self.operation == '÷':
                  if second_number == 0:
                      messagebox.showerror("Error", "Cannot divide by zero")
                      return
                  result = self.first_number / second_number

              self.display_var.set(str(round(result, 8)))
              self.first_number = result
              self.operation = None
              self.waiting_for_operand = True

          except Exception:
              messagebox.showerror("Error", "Invalid calculation")
              self.reset_calculator()
              self.display_var.set("0")

      def toggle_sign(self):
          try:
              value = float(self.display_var.get())
              self.display_var.set(str(-value))
          except:
              pass

      def percentage(self):
          try:
              value = float(self.display_var.get())
              result = value / 100
              self.display_var.set(str(result))
          except:
              pass

      def square_root(self):
          try:
              value = float(self.display_var.get())
              if value < 0:
                  messagebox.showerror("Error", "Cannot calculate square root of negative number")
              else:
                  result = math.sqrt(value)
                  self.display_var.set(str(round(result, 8)))
          except:
              messagebox.showerror("Error", "Invalid number")

  def main():
      root = tk.Tk()
      app = Calculator(root)
      root.mainloop()

  if __name__ == "__main__":
      main()
