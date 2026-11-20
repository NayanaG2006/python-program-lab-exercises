
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        file = open("students.txt", "a")
        file.write(name + "," + roll + "\n")
        file.close()

        print("Student added successfully!")

    elif choice == 2:
        file = open("students.txt", "r")
        print("\nStudent Details:")

        for line in file:
            print(line.strip())

        file.close()

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
