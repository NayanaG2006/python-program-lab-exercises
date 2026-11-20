
contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == 2:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 3:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
