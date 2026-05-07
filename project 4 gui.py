# TASK 4 : Rock-Paper-Scissors Game USING PYTHON TKINTER (GUI)

import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

# Global score
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Functions
def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    global user_score, computer_score
    if user == computer:
        return "🤝 It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        user_score += 1
        return "🎉 You Win!"
    else:
        computer_score += 1
        return "😢 You Lose!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"🧍‍♂️ You chose: {user_choice}", fg="white")
    comp_choice_label.config(text=f"💻 Computer chose: {computer_choice}", fg="white")
    result_label.config(text=result, fg="#00FF00" if "Win" in result else "#FF0000" if "Lose" in result else "orange")
    score_label.config(text=f"📊 Score - You: {user_score} | Computer: {computer_score}", fg="yellow")

# UI Components
title_label = tk.Label(root, text="✊🖐✌ Rock Paper Scissors", font=("Helvetica", 20, "bold"), bg="#1e1e1e", fg="cyan")
title_label.pack(pady=20)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

btn_style = {"font": ("Helvetica", 16), "width": 10, "height": 2, "bg": "#333", "fg": "black", "activebackground": "#555"}

rock_btn = tk.Button(btn_frame, text=" 🪨 Rock", command=lambda: play("Rock"), **btn_style)
paper_btn = tk.Button(btn_frame, text="📃 Paper", command=lambda: play("Paper"), **btn_style)
scissors_btn = tk.Button(btn_frame, text=" ✂️ Scissors", command=lambda: play("Scissors"), **btn_style)

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#1e1e1e")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#1e1e1e")
comp_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#1e1e1e")
result_label.pack(pady=10)

score_label = tk.Label(root, text="📊 Score - You: 0 | Computer: 0", font=("Helvetica", 16, "bold"), bg="#1e1e1e", fg="yellow")
score_label.pack(pady=15)

exit_button = tk.Button(root, text="🚪 Exit Game", command=root.quit, font=("Helvetica", 14), bg="#660000", fg="black", width=15)
exit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
