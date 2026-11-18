students = {}
# Add Student
def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))

    print("Enter marks of 3 subjects:")
    python = float(input("Python: "))
    maths = float(input("Mathematics: "))
    english = float(input("English: "))

    students[roll] = {
        "name": name,
        "age": age,
        "python": python,
        "maths": maths,
        "english": english
    }

    print("Student added successfully!")

# Search Student
def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        student = students[roll]

        print("\nStudent Record")
        print("Roll Number:", roll)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Python:", student["python"])
        print("Mathematics:", student["maths"])
        print("English:", student["english"])
    else:
        print("Student not found!")

# Update Student
def update_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        student = students[roll]

        student["name"] = input("Enter New Name: ")
        student["age"] = int(input("Enter New Age: "))
        student["python"] = float(input("Enter New Python Marks: "))
        student["maths"] = float(input("Enter New Mathematics Marks: "))
        student["english"] = float(input("Enter New English Marks: "))

        print("Student record updated successfully!")
    else:
        print("Student not found!")

# Delete Student
def delete_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# Display All Students
def display_students():
    if len(students) == 0:
        print("No student records available.")
        return

    print("\n===== ALL STUDENT RECORDS =====")

    for roll, student in students.items():
        print("\nRoll Number:", roll)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Python:", student["python"])
        print("Mathematics:", student["maths"])
        print("English:", student["english"])

# Calculate Total, Percentage and Average
def calculate_result():
    roll = input("Enter Roll Number: ")

    if roll in students:
        student = students[roll]

        total = (
            student["python"]
            + student["maths"]
            + student["english"]
        )

        percentage = (total / 300) * 100
        average = total / 3

        print("\n===== RESULT =====")
        print("Name:", student["name"])
        print("Roll Number:", roll)
        print("Total Marks:", total)
        print("Percentage:", percentage, "%")
        print("Average:", average)

    else:
        print("Student not found!")

# Main Menu
while True:

    print("\n========================================")
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Calculate Total, Percentage & Average")
    print("7. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_students()

    elif choice == "6":
        calculate_result()

    elif choice == "7":
        print("Thank you for using Student Record Management System!")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")
