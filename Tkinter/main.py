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


