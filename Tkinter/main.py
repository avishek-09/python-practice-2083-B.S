import tkinter as tk 

## ----Random Demo to undestand basics of tkinter-------
root = tk.Tk()
root.title("Demo")
root.geometry("600x400")

label1 = tk.Label(text = "Hello World!")
label2 = tk.Label(text = "I am learning Tkinter :)")
label3 = tk.Label(text = "Python is really getting interesting.")
label1.pack()
label2.pack()
label3.pack()

root.mainloop()

## ----Project for KM to Meter Converter------

root = tk.Tk()
root.title("KM to M Converter")
root.geometry("600x400")

def convert():
    km = float(input.get())
    meter = km * 1000
    result.config(text = f"In Meter: {meter}")

label1 = tk.Label(text = "Enter distance in KM: ", font = ("Arial", 13))
label1.place(x = 130 , y = 30)

input = tk.Entry()
input.place(x = 300, y = 33)

button = tk.Button(text = "Convert", command = convert)
button.place(x = 430 , y = 29)

result = tk.Label(text = "In Meter: ", font = ("Arial", 13))
result.place(x= 180 , y = 65)

root.mainloop()

