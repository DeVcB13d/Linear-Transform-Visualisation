#from tkinter import *
import tkinter as tk
window=tk.Tk(className=' Linear transform-Visualization')
window.geometry("400x200")
window.configure(bg="#E6E6FA")
window.iconbitmap('logo.jpg')

#Creating input fields
label=tk.Label(window,
            text="Vector operations",
            font=('Times new Roman',40,'bold'),
            fg='#0000FF',bg='#E6E6FA',
            )
label.pack()

#Creating buttons and entry fields
def Input_vector():
    
    v1=tk.Label(window,text="Enter vector 1: ",font=('calibre',10, 'bold'))
    v1.pack()
    e1=tk.Entry(window)
    e1.pack()
    v2=tk.Label(window,text="Enter vector 2: ",font=('calibre',10, 'bold'))
    v2.pack()
    e2=tk.Entry(window)
    e2.pack()

myButton1=tk.Button(window,text="Calculate",command=Input_vector())
myButton2=tk.Button(window,text="Run simulation")#command=myClick
myButton1.pack()
myButton2.pack()
#Input_vector()
window.mainloop()
