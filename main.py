print("Student Management System")
print("-------------------------")

print("1. Add Student")
print("2. View Student")
print("3. Search Student")
print("4. Exit")
print("5. Update student")
print("6. Delete student")


students = []

while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            course = input("enter Student Course: ")

            student = {
                "name": name,
                "age": age,
                "course" : course
            }

            students.append(student)

            print("Student added successfully")

        elif choice == "2":
            print("\nStudents Details:")

            if len(students) == 0:
                print("No students found.")
            else:
                for student in students:
                        print("Name:", student["name"])
                        print("Age:", student["age"])
                        print("Course:", student["course"])

        elif choice == "3":
            name = input("Enter Student name to search:")

            found = False

            for student in students:
                if student["name"].lower() == name.lower():
                    print("Student Found!")
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Course:", student["course"])
                    found = True

            if not found:
                print("Student not found.")        

        elif choice == "5":
            name = input("Enter student name to update:")

            found = False

            for student in students:
                if student["name"].lower() == name.lower():
                    student["age"] = input("Enter new age:")
                    student["course"] = input("Enter new course:")

                    print("Student updated successfully")
                    found = True
                    break

            if not found:
                print("Student not found.") 


        elif choice == "6":
            name = input("Enter student name to delete: ")

            found = False

            for student in students:
                if student["name"].lower() == name.lower():
                    students.remove(student)
                    print("Student deleted successfully")
                    found = True
                    break

                if not found:
                    print("Student not found.")    

        elif choice == "4":
            print("Thank you for using Student Management System! ")
            break

        else:
            print("Invalid choice")                


