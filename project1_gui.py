# TASK 1 : To-Do List Application using Python TKINTER (GUI) 
 

import tkinter as tk
from tkinter import messagebox

# Task list
tasks = []

# Add new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"title": task, "completed": False})
        task_entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Update task list display
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task['completed'] else "❌"
        task_listbox.insert(tk.END, f"{task['title']} - {status}")

# Mark selected task as completed
def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]['completed'] = True
        update_listbox()
    else:
        messagebox.showinfo("Info", "Please select a task to mark as completed.")

# Delete selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_title = tasks[index]['title']
        del tasks[index]
        update_listbox()
        messagebox.showinfo("Deleted", f"🗑️ Deleted task: {task_title}")
    else:
        messagebox.showinfo("Info", "Please select a task to delete.")

# GUI Setup
root = tk.Tk()
root.title("📝 To-Do List App")

# Task Entry Field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack()

# Listbox to show tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Buttons
complete_btn = tk.Button(root, text="Mark Completed", width=20, command=mark_completed)
complete_btn.pack(pady=2)

delete_btn = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_btn.pack(pady=2)

# Run the app
root.mainloop()
