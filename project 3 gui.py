# TASK 3 : PASSWORD GENERATOR USING PYTHON TKINTER (GUI)


import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length < 4:
            messagebox.showerror("Error", "Minimum length is 4.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("🔐 Cool Password Generator")
root.geometry("600x450")
root.configure(bg="#e8f0fe")  # Light bluish background

# Fonts
title_font = ("Verdana", 24, "bold")
label_font = ("Verdana", 16)
entry_font = ("Verdana", 16)
button_font = ("Verdana", 16, "bold")
result_font = ("Courier", 18, "bold")

# Title
tk.Label(root, text="✨ Password Generator ✨", font=title_font, bg="#e8f0fe", fg="#1f2937").pack(pady=20)

# Input Label
tk.Label(root, text="Enter Password Length", font=label_font, bg="#e8f0fe", fg="#1f2937").pack()

# Input Field
entry = tk.Entry(root, font=entry_font, justify="center", width=10, bd=3, relief="ridge", bg="#ffffff")
entry.pack(pady=15)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password,
          font=button_font, bg="#2563eb", fg="white", activebackground="#1d4ed8", padx=20, pady=10,
          relief="raised", bd=4).pack(pady=20)

# Result Label
tk.Label(root, text="Your Password:", font=label_font, bg="#e8f0fe", fg="#1f2937").pack()

result_label = tk.Label(root, text="", font=result_font, wraplength=550,
                        bg="#e8f0fe", fg="#10b981", justify="center")
result_label.pack(pady=10)

root.mainloop()
