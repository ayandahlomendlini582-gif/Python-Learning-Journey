import tkinter 
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox

def enter_data():

    accepted  = accept_var.get()

    if accepted=="Accepted":
        #User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        #Course Info
        registration_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemesters = numsemester_spinbox.get()


        print("First name: ", first_name, "Lastname: ", last_name)
        print("Title: ", title, "Age: ",age, "Nationality: ", nationality)
        print("# Courses: ", numcourses, "Semesters: ", numsemesters)
        print("Registration status", registration_status)
        print("----------------------------------------------------------------")

    else:
        tkinter.messagebox.showwarning(title= "Error", message="you have not accepted the terms")



    




window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#SAVING USER INFO
user_info_frame = tkinter.LabelFrame(frame, text="user information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name = tkinter.Label(user_info_frame, text='First Name')
first_name.grid(row=0, column=0)
last_name = tkinter.Label(user_info_frame, text='Last Name')
last_name.grid(row=0, column=1)


first_name_entry = tkinter.Entry(user_info_frame,)
last_name_entry = tkinter.Entry(user_info_frame,)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title" )
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "MS.", "DR."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)


age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

label_nationality = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa","Antartica", "Europe","Asia", "America"]) 
label_nationality.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#SAVING COURSE INFO
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not registered")
registered_check = tkinter.Checkbutton(courses_frame, 
                                       text="Currently Registered", 
                                       variable=reg_status_var, 
                                       onvalue="Registered",
                                       offvalue="Not registered")


registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

number_courses = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
number_courses.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemester_label = tkinter.Label(courses_frame, text="# Semesters")
numsemester_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemester_label.grid(row=0, column=2)
numsemester_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#ACCEPT TERMS
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20 ,pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, 
                                  text="I accept the terms and conditions.",
                                  variable=accept_var,
                                  onvalue="Accepted",
                                  offvalue="Not accepted")
terms_check.grid(row=0, column=0)


#BUTTON
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)





window.mainloop()

