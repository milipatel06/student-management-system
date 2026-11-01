import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

students = []

window.title("Student Management System")
window.geometry("600x500")
window.config(bg="#EAF2F8")
title_label = tk.Label(window, text = "Student Management System", font = ("Arial", 18, "bold"))
title_label.pack(pady=20)

# add student
def add_student():
    add_window = tk.Toplevel(window)  
    add_window.title("Add Student")
    add_window.geometry("400x300")
    add_window.config(bg = "#EAF2F8")
    add_title = tk.Label(add_window, text = "Add Student",bg = "#EAF2F8", font = ("Arial", 16, "bold"))
    add_title.pack(pady=15)

    name_label = tk.Label(add_window, text = "Student Name:",bg = "#EAF2F8")
    name_label.pack(pady=10)

    name_entry = tk.Entry(add_window,bg = "white",fg = "#333333")
    name_entry.pack(pady=5, ipadx=30)

    age_label = tk.Label(add_window, text = "Student Age:",bg = "#EAF2F8")
    age_label.pack(pady=10)

    age_entry = tk.Entry(add_window,bg = "white",fg = "#333333")
    age_entry.pack(pady=5, ipadx=30)

    course_label = tk.Label(add_window, text = "Student Course:",bg = "#EAF2F8")
    course_label.pack(pady=10)

    course_entry = tk.Entry(add_window,bg = "white",fg = "#333333")
    course_entry.pack(pady=5 , ipadx=30)

    

    def save_student():
         name = name_entry.get()
         age = age_entry.get()
         course = course_entry.get()

         if name == "" or age == "" or course == "":
            print("Please fill all feilds.")
            return

         if not age.isdigit():
            print("Age must be a number.")
            return   

         Student = {
             "name" : name,
             "age" : age,
             "course" : course
         }

         students.append(Student)
         messagebox.showinfo("Success", "Student added successfully!")
         add_window.destroy()

    save_button = tk.Button(add_window, text = "Add Student", command = save_student,bg = "#4CAF50",fg = "white",font = ("Arial",12, "bold"))
    save_button.pack(pady=15)     

add_button = tk.Button(window, text = "Add Students", command = add_student, font = ("Arial", 12), width = 15, height = 2, bg = "#4CAF50",fg = "white")
add_button.pack(pady=8)

# view students
def view_students():
    view_window = tk.Toplevel(window)
    view_window.title("View Students")
    view_window.geometry("400x300")
    view_window.config(bg = "#EAF2F8")

    if len(students) == 0:
        tk.Label(view_window, text = "No students found.").pack(pady=20)
        return

    for Student in students:
        Student_label = tk.Label(view_window, text = f"Name: {Student['name']}\nAge: {Student['age']}\nCourse: {Student['course']}")
        Student_label.pack(pady=10)

view_button = tk.Button(window, text = "View Students",font = ("Arial",12), width = 15, height = 2, bg = "#2196F3", fg = "white",command = view_students)
view_button.pack(pady=8)

# Search Students
def Search_student():
    Search_window = tk.Toplevel(window)
    Search_window.title("Search Student")
    Search_window.geometry("400x250")
    Search_window.config(bg ="#EAF2F8")

    search_label = tk.Label(Search_window, text = "Enter Student Name: ", bg= "#EAF2F8")
    search_label.pack(pady=10)

    search_entry = tk.Entry(Search_window)
    search_entry.pack(pady=5, ipadx=30)

    result_label= tk.Label(Search_window)
    result_label.pack(pady=10)

    def perform_search():
        name = search_entry.get()

        if name == "":
            result_label.config(text = "Please enter student name.")
            return

        for Student in students:
            if Student["name"].lower() == name.lower():
                result_label.config(text = f"Student Found!\nName : {Student['name']}\nAge : {Student['age']}\nCourse : {Student['course']}")
                return

        result_label.config(text= "Student not found.")    

    search_button = tk.Button(Search_window, text = "Search Student",bg= "#9C27B0",fg="white",font= ("Arial",12, "bold"), command= perform_search)
    search_button.pack(pady=15)

search_button = tk.Button(window, text = "Search Students",font = ("Arial",12), width = 15, height = 2,bg = "#9C27B0", fg = "white",command= Search_student)
search_button.pack(pady=8)

# update students
def update_student():
    update_window = tk.Toplevel(window)
    update_window.title("Update Student")
    update_window.geometry("400x300")
    update_window.config(bg = "#EAF2F8")

    update_label = tk.Label(update_window, text = "Enter Student Name: ",bg = "#EAF2F8")
    update_label.pack(pady=10)

    update_entry = tk.Entry(update_window)
    update_entry.pack(pady=5, ipadx=30)

    age_label = tk.Label(update_window,text = "Enter New Age: ",bg = "#EAF2F8")
    age_label.pack(pady=5)

    age_entry = tk.Entry(update_window)
    age_entry.pack(pady=5, ipadx=30)

    course_label = tk.Label(update_window,text = "Enter New Course: ",bg = "#EAF2F8")
    course_label.pack(pady=5)

    course_entry = tk.Entry(update_window)
    course_entry.pack(pady=5, ipadx=30)

    def perform_update():
        name = update_entry.get()

        if name == "":
            print("Please enter student name.")
            return

        for Student in students:
            if Student["name"].lower() == name.lower():
                Student["age"] = age_entry.get()
                Student["course"] = course_entry.get()

                messagebox.showinfo("Success", "Student updated successfully!")
                return

            messagebox.showinfo("Not Found.", "Student not found.")

    update_button = tk.Button(update_window, text = "Update Student",font = ("Arial",12), bg = "#FF9800", fg = "white",command= perform_update)
    update_button.pack(pady=15)            

update_button = tk.Button(window, text = "Update Students",font = ("Arial",12), width = 15, height = 2, bg = "#FF9800", fg = "white",command=update_student)
update_button.pack(pady=8)

# Delete students
def delete_student():
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Student")
    delete_window.geometry("400x300")
    delete_window.config(bg = "#EAF2F8")

    delete_label = tk.Label(delete_window,text = "Enter Student Name: ",bg = "#EAF2F8")
    delete_label.pack(pady=10)

    delete_entry = tk.Entry(delete_window)
    delete_entry.pack(pady=5, ipadx=30)

    def perform_delete():
        name = delete_entry.get()

        if name == "":
            print("Please enter student name.")
            return

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                messagebox.showinfo("Success", "Student deleted successfully!")

        messagebox.showinfo("Not Found", "Student not found.")

    delete_button = tk.Button(delete_window, text = "Delete Student",font = ("Arial",12), bg = "#F44336", fg = "white", command = perform_delete) 
    delete_button.pack(pady=15)           

delete_button = tk.Button(window, text = "Delete Students",font = ("Arial",12), width = 15, height = 2, bg = "#F44336", fg = "white",command = delete_student)
delete_button.pack(pady=8)

# Exit
exit_button = tk.Button(window, text = "Exit", command = window.destroy, font = ("Arial",12), width = 15, height = 2, bg = "#607D8B", fg = "white" )
exit_button.pack(pady=8)

window.mainloop()