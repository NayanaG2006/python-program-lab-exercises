
import csv

# Create CSV file
with open("payroll.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Basic Salary", "Bonus", "Total Salary"])

while True:
    print("\n1. Add Employee")
    print("2. Display Payroll")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter employee name: ")
        salary = int(input("Enter basic salary: "))
        bonus = int(input("Enter bonus: "))

        total = salary + bonus

        with open("payroll.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, salary, bonus, total])

        print("Employee added successfully!")

    elif choice == 2:
        with open("payroll.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
