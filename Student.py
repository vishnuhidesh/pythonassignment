# Suppose you are a teacher, you have to store student details. Write a program to enter and
# store student roll number and name. Use dictionary

student_details = {}
def add(roll_number, name):
    student_details[roll_number] = name

def display():
    print("Student Details:")
    for roll_number, name in student_details.items():
        print(f"Roll Number: {roll_number}, Name: {name}")

while True:
    print("\nOptions:")
    print("1. Add Student Details")
    print("2. Display Student Details")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        roll_number = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        add(roll_number, name)
        print("Student details added successfully!")
    elif choice == '2':
        display()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")