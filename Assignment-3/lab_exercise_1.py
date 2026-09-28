# Lab Exercise 1: Contact Book Using Lists and Dictionaries

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def display_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== CONTACT BOOK =====")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact found!")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return

    print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        display_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")