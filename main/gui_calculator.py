import tkinter as tk
from tkinter import messagebox
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display_frame = tk.Frame(self.root)
        display_frame.pack(pady=10)
        
        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 16),
            width=20,
            justify="right",
            state="readonly"
        )
        display.pack()
        
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        
        self.create_buttons(buttons_frame)
    
    def create_buttons(self, parent):
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '√']
        ]
        
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '0':
                    btn = tk.Button(
                        parent,
                        text=button_text,
                        font=("Arial", 14),
                        width=10,
                        height=2,
                        command=lambda t=button_text: self.on_button_click(t)
                    )
                    btn.grid(row=i, column=j, columnspan=2, padx=2, pady=2, sticky="ew")
                else:
                    btn = tk.Button(
                        parent,
                        text=button_text,
                        font=("Arial", 14),
                        width=5,
                        height=2,
                        command=lambda t=button_text: self.on_button_click(t)
                    )
                    btn.grid(row=i, column=j, padx=2, pady=2)
        
        extra_frame = tk.Frame(self.root)
        extra_frame.pack(pady=10)
        
        tk.Button(
            extra_frame,
            text="x²",
            font=("Arial", 12),
            width=8,
            command=lambda: self.on_button_click("x²")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            extra_frame,
            text="Clear",
            font=("Arial", 12),
            width=8,
            command=self.clear_all
        ).pack(side=tk.LEFT, padx=5)
    
    def on_button_click(self, button_text):
        try:
            if button_text in '0123456789':
                if self.expression == "0":
                    self.expression = button_text
                else:
                    self.expression += button_text
            
            elif button_text == '.':
                if '.' not in self.expression.split()[-1]:
                    self.expression += button_text
            
            elif button_text in ['+', '-']:
                self.expression += f' {button_text} '
            
            elif button_text == '×':
                self.expression += ' * '
            
            elif button_text == '÷':
                self.expression += ' / '
            
            elif button_text == '%':
                self.expression += ' % '
            
            elif button_text == 'C':
                self.clear_last()
            
            elif button_text == '±':
                self.toggle_sign()
            
            elif button_text == '=':
                self.calculate()
            
            elif button_text == '√':
                self.square_root()
            
            elif button_text == 'x²':
                self.square()
            
            self.update_display()
            
        except Exception as e:
            messagebox.showerror("Помилка", f"Сталася помилка: {e}")
    
    def clear_last(self):
        if self.expression:
            self.expression = self.expression[:-1]
        if not self.expression:
            self.expression = "0"
    
    def clear_all(self):
        self.expression = "0"
        self.update_display()
    
    def toggle_sign(self):
        try:
            if self.expression and self.expression != "0":
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
        except Exception:
            pass
    
    def calculate(self):
        try:
            calc_expression = self.expression.replace('×', '*').replace('÷', '/')
            result = eval(calc_expression)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Помилка", "Ділення на нуль!")
            self.expression = "0"
        except Exception:
            messagebox.showerror("Помилка", "Неправильний вираз!")
            self.expression = "0"
    
    def square_root(self):
        try:
            if self.expression:
                number = float(self.expression)
                if number < 0:
                    messagebox.showerror("Помилка", "Не можна взяти корінь з від'ємного числа!")
                else:
                    result = math.sqrt(number)
                    self.expression = str(result)
        except Exception:
            messagebox.showerror("Помилка", "Неправильне число!")
    
    def square(self):
        try:
            if self.expression:
                number = float(self.expression)
                result = number ** 2
                self.expression = str(result)
        except Exception:
            messagebox.showerror("Помилка", "Неправильне число!")
    
    def update_display(self):
        display_text = self.expression if self.expression else "0"
        self.display_var.set(display_text)


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
