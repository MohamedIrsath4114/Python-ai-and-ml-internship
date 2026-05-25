# Student Management System

students = []

# Function to add student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    marks_tuple = tuple(marks)

    student = {
        "name": name,
        "age": age,
        "marks": marks_tuple
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to display students
def display_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Name : {student['name']}")
        print(f"Age  : {student['age']}")
        print(f"Marks: {student['marks']}")

        avg = calculate_average(student['marks'])
        print(f"Average Marks: {avg:.2f}")
        print("-----------------------")


# Function to calculate average marks
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


# Function to find topper
def find_topper():
    if len(students) == 0:
        print("No student records found.\n")
        return

    topper = students[0]
    highest_avg = calculate_average(topper['marks'])

    for student in students:
        avg = calculate_average(student['marks'])

        if avg > highest_avg:
            highest_avg = avg
            topper = student

    print("\n--- Topper Details ---")
    print(f"Name : {topper['name']}")
    print(f"Age  : {topper['age']}")
    print(f"Marks: {topper['marks']}")
    print(f"Average Marks: {highest_avg:.2f}\n")


# Main Menu using while loop
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        display_students()

    elif choice == '3':
        find_topper()

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")
