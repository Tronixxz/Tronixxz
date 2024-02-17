# Student Management System

# Dictionary to store student records
students = {}

# Function to add a new student
def add_student():
    roll_number = input("Enter student roll number: ")
    name = input("Enter student name: ")
    students[roll_number] = name
    print("Student added successfully!")

# Function to view all students
def view_students():
    if students:
        print("List of Students:")
        for roll_number, name in students.items():
            print(f"Roll Number: {roll_number}, Name: {name}")
    else:
        print("No students found.")

# Function to delete a student
def delete_student():
    roll_number = input("Enter the roll number of the student to delete: ")
    if roll_number in students:
        del students[roll_number]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
