#!/usr/bin/env python3
"""
Simple GUI Calculator - Clean Test Application
Perfect for testing GitHub-to-EXE converter with windowed mode
No console input needed - pure GUI interface
"""

import tkinter as tk
from tkinter import messagebox
import math
import ast
import operator

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI Calculator")
        self.root.geometry("350x400")
        self.root.resizable(False, False)

        # Configure style
        self.root.configure(bg='#f0f0f0')

        self.create_widgets()
        self.current_expression = ""  # Track full expression

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
            width=5,
            height=2,
            bg=bg_color,
            fg=fg_color,
            command=lambda: self.button_click(text)
        )
        button.grid(row=row, column=col, padx=2, pady=2)

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
        if num == '.':
            # Prevent multiple decimal points in a number
            current = self.current_expression
            if current and current[-1].isdigit():
                last_num = ''.join(takewhile(lambda c: c.isdigit() or c == '.', current[::-1]))[::-1]
                if '.' in last_num:
                    return
        current = self.display_var.get()
        if current == "0" and num != '.':
            self.current_expression = num
        else:
            self.current_expression += num
        self.display_var.set(self.current_expression or "0")

    def handle_operator(self, op):
        current = self.current_expression
        if not current:
            return
        # Prevent consecutive operators
        if current[-1] in '+-*/':
            self.current_expression = current[:-1] + op
        else:
            self.current_expression += op
        self.display_var.set(self.current_expression)

    def calculate(self):
        try:
            # Convert display operators to Python operators
            expression = self.current_expression.replace('÷', '/').replace('×', '*')
            # Safely evaluate using ast.literal_eval
            result = self.safe_eval(expression)
            self.current_expression = str(round(float(result), 4))
            self.display_var.set(self.current_expression)
        except (ValueError, SyntaxError, ZeroDivisionError) as e:
            messagebox.showerror("Error", f"Invalid calculation: {str(e)}")
            self.current_expression = ""
            self.display_var.set("0")

    def safe_eval(self, expr):
        """Safely evaluate a mathematical expression using ast"""
        # Define allowed operators
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        def eval_node(node):
            if isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.BinOp):
                left = eval_node(node.left)
                right = eval_node(node.right)
                op = ops.get(type(node.op).__name__)
                if not op:
                    raise ValueError("Unsupported operator")
                return op(left, right)
            else:
                raise ValueError("Invalid expression")

        parsed = ast.parse(expr, mode='eval')
        return eval_node(parsed.body)

    def toggle_sign(self):
        try:
            value = float(self.current_expression or "0")
            self.current_expression = str(-value)
            self.display_var.set(self.current_expression)
        except ValueError:
            pass

    def percentage(self):
        try:
            value = float(self.current_expression or "0")
            result = value / 100
            self.current_expression = str(round(result, 4))
            self.display_var.set(self.current_expression)
        except ValueError:
            pass

    def square_root(self):
        try:
            value = float(self.current_expression or "0")
            if value < 0:
                messagebox.showerror("Error", "Cannot calculate square root of negative number")
            else:
                result = math.sqrt(value)
                self.current_expression = str(round(result, 4))
                self.display_var.set(self.current_expression)
        except ValueError:
            messagebox.showerror("Error", "Invalid number")

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
