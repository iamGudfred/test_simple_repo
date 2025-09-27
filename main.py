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
          self.root.geometry("350x450")  # Made taller
          self.root.resizable(False, False)

          # Configure style
          self.root.configure(bg='#f0f0f0')

          self.create_widgets()
          self.current_expression = ""

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

          # Button layout - Fixed layout
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
              width=6,  # Made buttons wider
              height=2,
              bg=bg_color,
              fg=fg_color,
              command=lambda: self.button_click(text)
          )
          button.grid(row=row, column=col, padx=3, pady=3)

      def button_click(self, value):
          if value == 'C':
              self.current_expression = ""
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
          if self.current_expression == "0":
              self.current_expression = num
          else:
              self.current_expression += num
          self.display_var.set(self.current_expression)

      def handle_operator(self, op):
          if self.current_expression and self.current_expression[-1] not in '+-*/':
              # Convert display operators to Python operators
              op_map = {'÷': '/', '×': '*'}
              python_op = op_map.get(op, op)
              self.current_expression += python_op
              self.display_var.set(self.current_expression)

      def calculate(self):
          try:
              # Simple and safe evaluation
              result = eval(self.current_expression)
              self.current_expression = str(round(result, 8))
              self.display_var.set(self.current_expression)
          except Exception:
              messagebox.showerror("Error", "Invalid calculation")
              self.current_expression = ""
              self.display_var.set("0")

      def toggle_sign(self):
          try:
              if self.current_expression:
                  value = float(self.current_expression)
                  self.current_expression = str(-value)
                  self.display_var.set(self.current_expression)
          except:
              pass

      def percentage(self):
          try:
              if self.current_expression:
                  value = float(self.current_expression)
                  result = value / 100
                  self.current_expression = str(result)
                  self.display_var.set(self.current_expression)
          except:
              pass

      def square_root(self):
          try:
              if self.current_expression:
                  value = float(self.current_expression)
                  if value < 0:
                      messagebox.showerror("Error", "Cannot calculate square root of negative number")
                  else:
                      result = math.sqrt(value)
                      self.current_expression = str(result)
                      self.display_var.set(self.current_expression)
          except:
              messagebox.showerror("Error", "Invalid number")

  def main():
      root = tk.Tk()
      app = Calculator(root)
      root.mainloop()

  if __name__ == "__main__":
      main()
