import tkinter as tk
from tkinter import ttk, messagebox 
import sqlite3

def enter_data():
    accepted = accept_var.get()


    if accepted == "Accepted":
        # User info
        empid = emp_id_entry.get()
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if  firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            gender = gender_combobox.get()
            
            print("Employee Id: ", empid)
            print("First name: ", firstname)
            print("Last name: ", lastname)
            print("Title: ", title)
            print("Age: ", age,)
            print("Gender: ", gender)
            print("------------------------------------------")
            
        # Create Table
            conn = sqlite3.connect('ramya2.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Employee_Data
            (empid INT, firstname TEXT, lastname TEXT, title TEXT, age INT, gender TEXT)'''
            conn.execute(table_create_query)

            # Insert Data
            demod_insert_query = '''INSERT INTO Employee_Data (empid, firstname, lastname, title,
            age, gender) VALUES(?, ?, ?, ?, ?, ?)'''
            demod_insert_tuple = (empid, firstname, lastname, title, age, gender)
            cursor = conn.cursor()
            cursor.execute(demod_insert_query, demod_insert_tuple)
            conn.commit()
            conn.close()
            
            # Show the entered data
            messagebox.showinfo("Entered Data", f"Employee Id: {empid}\nFirst Name: {firstname}\nLast Name: {lastname}\nTitle: {title}\nAge: {age}\nGender: {gender}")
            print("Data Entered Successfully!")
            
            
        else:
            messagebox.showwarning(title="Error", message="Employee id, First name and last name are required.")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms")

def retrieve_data():
    conn = sqlite3.connect('ramya2.db')
    cursor = conn.cursor()
    
    # Retrieve all data
    cursor.execute("SELECT * FROM Employee_Data")
    records = cursor.fetchall()
    
    conn.close()


    # Format the retrieved data
    if records:
        data_string = "\n".join([f"Employee Id: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, Title: {record[3]}, Age: {record[4]}, Gender: {record[5]}" for record in records])
        messagebox.showinfo("All Data Entered", data_string)
    else:
        messagebox.showinfo("All Data Entered", "No data found.")          
            



window = tk.Tk()
window.title("STARTUP COMPANY")

frame = tk.Frame(window, bg="light blue", bd=2, relief=tk.SUNKEN)
frame.pack()

employee_profile=tk.LabelFrame(frame, text="employee profile")
employee_profile.grid(row=0, column=0, padx=10, pady=20)

emp_id=tk.Label(employee_profile, text="Employee Id")
emp_id.grid(row=0, column=0)

first_name=tk.Label(employee_profile, text="First Name")
first_name.grid(row=0, column=1)

last_name=tk.Label(employee_profile, text="Last Name")
last_name.grid(row=0, column=2)

emp_id_entry=tk.Entry(employee_profile)
emp_id_entry.grid(row=1, column=0,padx=10, pady=20)
first_name_entry=tk.Entry(employee_profile)
first_name_entry.grid(row=1, column=1,padx=10, pady=20)
last_name_entry=tk.Entry(employee_profile)
last_name_entry.grid(row=1, column=2, padx=10, pady=20)

title_name=tk.Label(employee_profile, text = "Title")
title_combobox = ttk.Combobox(employee_profile, values=["Senior Developer", "Junior Developer",
                                                     "Human Resources", "Sales representatives"])
title_name.grid(row=0, column=3)
title_combobox.grid(row=1, column=3)


age_label=tk.Label(employee_profile, text="Age")
age_spinbox=tk.Spinbox(employee_profile, from_=18, to=60)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


gender=tk.Label(employee_profile, text = "Gender")
gender_combobox = ttk.Combobox(employee_profile, values=["Male", "Female", "Others"])
gender.grid(row=2, column=1)
gender_combobox.grid(row=3, column=1)


for widget in employee_profile.winfo_children():
    widget.grid_configure(padx=10, pady=5) 
    
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)  # Changed to row=1

# Optional: Add content to terms_frame for visibility
terms_label = tk.Label(terms_frame, text="Please read the terms and conditions.")
terms_label.grid(row=0, column=0, padx=10, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                   variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=2, column=0)

# Allow the frame to expand
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

button = tk.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# New button to retrieve data
retrieve_button = tk.Button(frame, text="Retrieve Data", command=retrieve_data)
retrieve_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

window.mainloop()