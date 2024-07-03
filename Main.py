import os
import json

CONTACTS_FILE = 'contacts.json' #name of the file storing contacts

def load_contacts():
    #Checking if file exists
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    #dictionary written to file
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    provider = input("Enter network provider: ")
    contacts.append({'name': name, 'phone': phone, 'provider': provider})
    #Updated file
    save_contacts(contacts)
    print("Contact added successfully!")

def search_by_phone(contacts):
    phone = input("Enter phone number to search: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print(f"Name: {contact['name']}, Provider: {contact['provider']}")
            return
    print("No contact found with that phone number.")

def search_by_name(contacts):
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Phone: {contact['phone']}, Provider: {contact['provider']}")
            found = True
    if not found:
        print("No contact found with that name.")

def search_by_provider(contacts):
    provider = input("Enter network provider to search: ")
    found = False
    for contact in contacts:
        if contact['provider'].lower() == provider.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
    if not found:
        print("No contacts found with that network provider.")

def delete_contact(contacts):
    phone = input("Enter phone number of the contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            #Updated file
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("No contact found with that phone number.")

def main():
    #Loaded contacts from file
    contacts = load_contacts()
    print(contacts)

    while True:
        print("\nContact Management System")
        print("1. Add new contact")
        print("2. Search by phone number")
        print("3. Search by name")
        print("4. Search by network provider")
        print("5. Delete a contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_by_phone(contacts)
        elif choice == '3':
            search_by_name(contacts)
        elif choice == '4':
            search_by_provider(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
