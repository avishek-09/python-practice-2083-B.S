import tkinter as tk 

## ----Random Demo to undestand basics of tkinter-------
# root = tk.Tk()
# root.title("Demo")
# root.geometry("600x400")

# label1 = tk.Label(text = "Hello World!")
# label2 = tk.Label(text = "I am learning Tkinter :)")
# label3 = tk.Label(text = "Python is really getting interesting.")
# label1.pack()
# label2.pack()
# label3.pack()

# root.mainloop()

## ----Project for KM to Meter Converter------

# root = tk.Tk()
# root.title("KM to M Converter")
# root.geometry("600x400")

# def convert():
#     km = float(input.get())
#     meter = km * 1000
#     result_box.delete(0, tk.END)
#     result_box.insert(0, meter)

# label1 = tk.Label(text = "Enter distance in KM: ", font = ("Arial", 13))
# label1.place(x = 130 , y = 30)

# input_box = tk.Entry()
# input_box.place(x = 300, y = 33)

# button = tk.Button(text = "Convert", command = convert)
# button.place(x = 430 , y = 29)

# label2 = tk.Label(text = "In Meter: ", font = ("Arial", 13))
# label2.place(x= 224 , y = 65)

# result_box = tk.Entry()
# result_box.place(x = 300, y= 68)

# root.mainloop()



## ----Project for login and Register------
import csv
from tkinter import messagebox

def register_to_csv():
    global label1_input_box, label3_input_box, label2_input_box
    username =  label1_input_box.get()
    email = label3_input_box.get()
    password = label2_input_box.get()

    if not (username or email or password):
        messagebox.showerror("Validation Error", "All fields are required.")
        
    with open("register.csv", "a", newline = "") as file: 
        writer = csv.writer(file)
        writer.writerow([username, email, password])

    login_widget()

def clear_widget():
    for widget in root.winfo_children():
        widget.destroy()

def login_widget():
    clear_widget()

    global label1_input_box, label2_input_box

    title_label = tk.Label(text = "Login To Your Account", font = ("arial", 20))
    title_label.pack()

    label1 = tk.Label(text = "Username: ",font =("arial", 15) )
    label1.place(x = 250,y=70)

    label1_input_box = tk.Entry(width = 30)
    label1_input_box.place(x=353,y= 75) 

    label2 = tk.Label(text= "Password: ", font = ("arial", 15 ) )
    label2.place(x= 250,y= 120)

    label2_input_box = tk.Entry(width = 30, show = "*")
    label2_input_box.place(x=353, y= 125) 

    login_button = tk.Button(text = "Login", font = ("arial", 12 ), padx = 30, pady= 4)
    login_button.place(x = 365 , y = 165 )

    Signup_button = tk.Button(text = "Sign Up", font = ("arial", 12 ), padx = 30, pady= 4, command = register_widget)
    Signup_button.place(x = 355 , y = 215)

##--------------------------------------------------

def register_widget():
    clear_widget()
    global label1_input_box, label3_input_box, label2_input_box

    title_label = tk.Label(text = "Register And Sign UP", font = ("arial", 20))
    title_label.pack()

    label1 = tk.Label(text = "Username: ",font =("arial", 15) )
    label1.place(x = 250,y=70)

    label1_input_box = tk.Entry(width = 30)
    label1_input_box.place(x=353,y= 75) 

    label3 = tk.Label(text = "Email: ",font =("arial", 15) )
    label3.place(x = 288,y=120)

    label3_input_box = tk.Entry(width = 30)
    label3_input_box.place(x=353,y= 125) 

    label2 = tk.Label(text= "Password: ", font = ("arial", 15 ) )
    label2.place(x= 250,y= 170)

    label2_input_box = tk.Entry(width = 30, show = "*")
    label2_input_box.place(x=353, y= 175) 

    Signup_button = tk.Button(text = "Sign Up", font = ("arial", 12 ), padx = 30, pady= 4, command = register_to_csv)
    Signup_button.place(x = 355 , y = 215)

    login_button = tk.Button(text = "Login", font = ("arial", 12 ), padx = 30, pady= 4, command = login_widget)
    login_button.place(x = 365 , y = 270 )

root = tk.Tk()
root.title("Login or Sign Up")
root.geometry("800x400")

login_widget()
# register_widget()

root.mainloop()