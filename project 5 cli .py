#TASK 5 :Contact Book USING PYTHON (CLI)


import json
import os

# Contact Book File
FILENAME = "contact_book.json"

# Load contacts from file or create empty list
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("\n✅ Contact Added Successfully!\n")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("\n⚠️ No contacts found.\n")
    else:
        print("\n📒 All Contacts:\n")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}\n")

# Search a contact
def search_contact():
    keyword = input("Enter Name to Search: ")
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if contact['name'].lower() == keyword.lower():
            print("\n🔍 Contact Found:\n")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
    if not found:
        print("\n❌ Contact not found.\n")

# Update contact
def update_contact():
    keyword = input("Enter Name to Update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == keyword.lower():
            print("\n🛠️ Updating Contact...")
            contact['name'] = input("New Name: ")
            contact['phone'] = input("New Phone Number: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")
            save_contacts(contacts)
            print("\n✅ Contact Updated Successfully!\n")
            return
    print("\n❌ Contact not found.\n")

# Delete contact
def delete_contact():
    keyword = input("Enter Name to Delete: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == keyword.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("\n🗑️ Contact Deleted Successfully!\n")
            return
    print("\n❌ Contact not found.\n")

# Menu
def menu():
    while True:
        print("====== 📞 Contact Book Menu ======")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n👋 Exiting Contact Book. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice. Try again.\n")

# Run Program
menu()
