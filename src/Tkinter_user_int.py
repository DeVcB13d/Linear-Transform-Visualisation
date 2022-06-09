# from tkinter import *
import tkinter as tk
from tkinter import CENTER

window = tk.Tk(className=' Linear transform-Visualization')
window.geometry("800x400")
window.configure(bg="#E6E6FA")
# setting background image
bg = tk.PhotoImage(file="bg1.png")
label = tk.Label(window, image=bg, width=1280, height=720)
label.place(x=0, y=0)
# icon image
photo = tk.PhotoImage(file="logo.png")
window.iconphoto(False, photo)
# Creating input fields
label1 = tk.Label(window,
                  text="Vector operations",
                  font=('Times new Roman', 30, 'bold'),
                  fg='#DC5539', bg='#000000',
                  )
label1.place(x=640, y=360)
label1.pack()


# Creating buttons and entry fields
def Input_vector():
    frame1 = tk.Frame(window, highlightbackground="blue", highlightthickness=2, bg="black")
    frame1.pack(padx=100, pady=100)
    v1 = tk.Label(frame1, text="Enter vector 1: ", font=('calibre', 10, 'bold'), fg='#E6E6FA', bg='#000000')
    v1.pack(padx=0, pady=10)
    e1 = tk.Entry(frame1, width=50, justify=CENTER)
    e1.pack()
    v2 = tk.Label(frame1, text="Enter vector 2: ", font=('calibre', 10, 'bold'), fg='#E6E6FA', bg='#000000')
    v2.pack(padx=0, pady=10)
    e2 = tk.Entry(frame1, width=50, justify=CENTER)
    e2.pack()


myButton1 = tk.Button(window, text="Calculate", command=Input_vector())
myButton2 = tk.Button(window, text="Run simulation")  # command=myClick
myButton1.pack()
myButton2.pack()
# Input_vector()
window.mainloop()

