
name = input("Enter student name: ")

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)
