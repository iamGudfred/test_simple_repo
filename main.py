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
                  btn = tk.Button(
                      button_frame,
                      text=btn_text,
                      font=("Arial", 14),
                      width=6,
                      height=2,
                      command=lambda t=btn_text: self.button_click(t),
                      bg='#e0e0e0',
                      activebackground='#d0d0d0'
                  )
                  btn.grid(row=i, column=j, padx=2, pady=2)

          # About button
          about_btn = tk.Button(
              self.root,
              text="About",
              font=("Arial", 10),
              command=self.show_about,
              bg='#cccccc',
              width=10
          )
          about_btn.pack(pady=10)

      def button_click(self, value):
          current = self.display_var.get()

          if value == 'C':
              self.reset_calculator()
          elif value == '=':
              self.calculate_result()
          elif value == '±':
              self.toggle_sign()
          elif value == '√':
              self.calculate_sqrt()
          elif value == '%':
              self.calculate_percentage()
          elif value in ['÷', '×', '+', '-']:
              self.handle_operator(value)
          else:
              self.handle_number(value)

      def handle_number(self, value):
          current = self.display_var.get()
          if current == "0" or current == "Error":
              self.display_var.set(value)
          else:
              self.display_var.set(current + value)

      def handle_operator(self, operator):
          try:
              self.first_number = float(self.display_var.get())
              self.operator = operator
              self.display_var.set("0")
          except ValueError:
              self.display_var.set("Error")

      def calculate_result(self):
          try:
              second_number = float(self.display_var.get())

              if self.operator == '+':
                  result = self.first_number + second_number
              elif self.operator == '-':
                  result = self.first_number - second_number
              elif self.operator == '×':
                  result = self.first_number * second_number
              elif self.operator == '÷':
                  if second_number == 0:
                      self.display_var.set("Error")
                      return
                  result = self.first_number / second_number
              else:
                  return

              # Format result
              if result == int(result):
                  self.display_var.set(str(int(result)))
              else:
                  self.display_var.set(f"{result:.8g}")

          except (ValueError, AttributeError):
              self.display_var.set("Error")

      def toggle_sign(self):
          try:
              current = float(self.display_var.get())
              self.display_var.set(str(-current))
          except ValueError:
              pass

      def calculate_sqrt(self):
          try:
              current = float(self.display_var.get())
              if current < 0:
                  self.display_var.set("Error")
              else:
                  result = math.sqrt(current)
                  if result == int(result):
                      self.display_var.set(str(int(result)))
                  else:
                      self.display_var.set(f"{result:.8g}")
          except ValueError:
              self.display_var.set("Error")

      def calculate_percentage(self):
          try:
              current = float(self.display_var.get())
              result = current / 100
              self.display_var.set(str(result))
          except ValueError:
              self.display_var.set("Error")

      def reset_calculator(self):
          self.display_var.set("0")
          self.first_number = 0
          self.operator = None

      def show_about(self):
          messagebox.showinfo(
              "About",
              "Simple GUI Calculator\n\n"
              "Built for GitHub-to-EXE converter testing\n"
              "Perfect for windowed mode (no console)\n\n"
              "Features: Basic arithmetic, square root, percentage"
          )

  def main():
      root = tk.Tk()
      app = Calculator(root)
      root.mainloop()

  if __name__ == "__main__":
      main()
