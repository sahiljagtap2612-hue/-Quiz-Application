import csv
import os

FILE_NAME = "students.csv"


# Create file if not exists
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Marks", "Subject"])


# Add Student
def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    subject = input("Enter Subject: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, marks, subject])

    print("✅ Student Added Successfully!")


# View Students
def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        print("\n--- Student Records ---")
        for row in reader:
            print(row)


# Search Student
def search_student():
    search_name = input("Enter student name to search: ")
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0].lower() == search_name.lower():
                print("Student Found:", row)
                found = True

    if not found:
        print("❌ Student Not Found")



def delete_student():
    delete_name = input("Enter student name to delete: ")
    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0].lower() != delete_name.lower():
                rows.append(row)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("✅ Student Deleted Successfully!")



def menu():
    create_file()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()

        elif choice == '2':
            view_students()

        elif choice == '3':
            search_student()

        elif choice == '4':
            delete_student()

        elif choice == '5':
            print("Thank You!")
            break

        else:
            print("❌ Invalid Choice")


menu()