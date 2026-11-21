import requests
import json
import os

API_URL = "https://jsonplaceholder.typicode.com/users"


# Get students from API
def get_students():

    # Check if local file exists
    if os.path.exists("students.json"):

        with open("students.json", "r") as file:
            students = json.load(file)

        print("Students loaded from local file!")
        return students

    # If file doesn't exist, get students from API
    response = requests.get(API_URL)
    response.raise_for_status()

    students = response.json()

    # Save API students locally
    save_students(students)

    return students
# Add a student
def add_student(name, email):
    new_student = {
        "name": name,
        "email": email
    }

    response = requests.post(API_URL, json=new_student)
    response.raise_for_status()

    return response.json()


# Display all students
def view_students(students):
    print("\n========== ALL STUDENTS ==========")

    for student in students:
        print(f"\nStudent ID : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Email      : {student['email']}")

        if "address" in student:
            print(f"City       : {student['address']['city']}")

        print("--------------------------------")


# Search for a student
def search_student(students):
    search_name = input("\nEnter student name: ")

    found = False

    for student in students:
        if search_name.lower() == student["name"].lower():

            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Email:", student["email"])

            if "address" in student:
                print("City:", student["address"]["city"])

            found = True
            break

    if not found:
        print("Student not found.")


# Add a new student
def create_student(students):
    print("\n========== ADD NEW STUDENT ==========")

    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    if email == "":
        print("Email cannot be empty!")
        return

    if "@" not in email:
        print("Invalid email address!")
        return

    try:
        result = add_student(name, email)

        print("\nStudent successfully added!")
        print("Name:", result["name"])
        print("Email:", result["email"])
        print("ID:", result["id"])

        students.append(result)
        save_students(students)

    except requests.exceptions.RequestException as error:
        print("\nFailed to add student.")
        print("Error:", error)


def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Students saved successfully!")

# Main program
def main():

    try:
        students = get_students()

    except requests.exceptions.RequestException as error:
        print("Failed to load students.")
        print("Error:", error)
        return

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. View all students")
        print("2. Search student")
        print("3. Add student")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_students(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            create_student(students)

        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


# Start program
main()