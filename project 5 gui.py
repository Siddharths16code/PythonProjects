# #TASK 5 : Contact Book USING PYTHON TKINTER (GUI)

# import tkinter as tk
# from tkinter import messagebox, simpledialog
# from tkinter import ttk

# # Contact storage
# contacts = {}

# # Core functions
# def add_contact():
#     name = entry_name.get()
#     phone = entry_phone.get()
#     email = entry_email.get()
#     address = entry_address.get()

#     if name and phone:
#         contacts[name] = {
#             "phone": phone,
#             "email": email,
#             "address": address
#         }
#         messagebox.showinfo("Success", f"Contact '{name}' added!")
#         clear_entries()
#         view_contacts()
#     else:
#         messagebox.showerror("Error", "Name and Phone are required.")

# def view_contacts():
#     listbox.delete(0, tk.END)
#     for name, info in contacts.items():
#         display = f"{name} - {info['phone']}"
#         listbox.insert(tk.END, display)

# def search_contact():
#     query = simpledialog.askstring("Search", "Enter name or phone to search:")
#     if not query:
#         return

#     listbox.delete(0, tk.END)
#     found = False
#     for name, info in contacts.items():
#         if query.lower() in name.lower() or query in info['phone']:
#             listbox.insert(tk.END, f"{name} - {info['phone']}")
#             found = True
#     if not found:
#         messagebox.showinfo("Not Found", "No matching contact found.")

# def delete_contact():
#     selected = listbox.get(tk.ACTIVE)
#     if selected:
#         name = selected.split(" - ")[0]
#         if name in contacts:
#             del contacts[name]
#             messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
#             view_contacts()
#     else:
#         messagebox.showwarning("Select Contact", "Please select a contact to delete.")

# def update_contact():
#     selected = listbox.get(tk.ACTIVE)
#     if selected:
#         name = selected.split(" - ")[0]
#         if name in contacts:
#             new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=contacts[name]["phone"])
#             new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contacts[name]["email"])
#             new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contacts[name]["address"])
            
#             contacts[name] = {
#                 "phone": new_phone,
#                 "email": new_email,
#                 "address": new_address
#             }
#             messagebox.showinfo("Updated", f"Contact '{name}' updated.")
#             view_contacts()
#     else:
#         messagebox.showwarning("Select Contact", "Please select a contact to update.")

# def clear_entries():
#     entry_name.delete(0, tk.END)
#     entry_phone.delete(0, tk.END)
#     entry_email.delete(0, tk.END)
#     entry_address.delete(0, tk.END)

# # GUI setup
# root = tk.Tk()
# root.title("📒 Contact Book")
# root.geometry("600x500")
# root.configure(bg="#f0f0f0")

# title = tk.Label(root, text="Contact Book", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
# title.pack(pady=10)

# frame_form = tk.Frame(root, bg="#f0f0f0")
# frame_form.pack(pady=10)

# tk.Label(frame_form, text="Name:", font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=0, column=0, padx=5, pady=5, sticky="e")
# entry_name = tk.Entry(frame_form, width=30)
# entry_name.grid(row=0, column=1, pady=5)

# tk.Label(frame_form, text="Phone:", font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=1, column=0, padx=5, pady=5, sticky="e")
# entry_phone = tk.Entry(frame_form, width=30)
# entry_phone.grid(row=1, column=1, pady=5)

# tk.Label(frame_form, text="Email:", font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=2, column=0, padx=5, pady=5, sticky="e")
# entry_email = tk.Entry(frame_form, width=30)
# entry_email.grid(row=2, column=1, pady=5)

# tk.Label(frame_form, text="Address:", font=("Arial", 12), bg="#f0f0f0", fg="black").grid(row=3, column=0, padx=5, pady=5, sticky="e")
# entry_address = tk.Entry(frame_form, width=30)
# entry_address.grid(row=3, column=1, pady=5)

# frame_buttons = tk.Frame(root, bg="#f0f0f0")
# frame_buttons.pack(pady=10)

# tk.Button(frame_buttons, text="➕ Add", command=add_contact, width=10, font=("Arial", 11)).grid(row=0, column=0, padx=5)
# tk.Button(frame_buttons, text="🔍 Search", command=search_contact, width=10, font=("Arial", 11)).grid(row=0, column=1, padx=5)
# tk.Button(frame_buttons, text="📋 View All", command=view_contacts, width=10, font=("Arial", 11)).grid(row=0, column=2, padx=5)
# tk.Button(frame_buttons, text="✏️ Update", command=update_contact, width=10, font=("Arial", 11)).grid(row=0, column=3, padx=5)
# tk.Button(frame_buttons, text="❌ Delete", command=delete_contact, width=10, font=("Arial", 11)).grid(row=0, column=4, padx=5)

# # List display
# listbox = tk.Listbox(root, width=60, height=12, font=("Courier New", 11))
# listbox.pack(pady=20)

# # Run the app
# root.mainloop()
