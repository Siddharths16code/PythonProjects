# TASK 2 : simple calculator USING PYTHON TKINTER 

import tkinter as tk

def press(key):
    entry_field.insert(tk.END, key)

def clear():
    entry_field.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry field to show input/output
entry_field = tk.Entry(window, width=20, font=('Arial', 18), bd=5)
entry_field.grid(row=0, column=0, columnspan=4)

# Buttons list
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons dynamically
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: calculate() if x == '=' else press(x)
    tk.Button(window, text=button, width=5, height=2, font=('Arial', 18),
              command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(window, text='C', width=21, height=2, font=('Arial', 18),
          command=clear).grid(row=row_val, column=0, columnspan=4)

# Run the GUI app
window.mainloop()

