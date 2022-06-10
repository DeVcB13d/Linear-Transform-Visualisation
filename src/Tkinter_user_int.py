# from tkinter import *
import tkinter as tk
from tkinter import CENTER, LEFT, RIGHT

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
label1.place(x=540, y=360)
label1.pack()

frame1 = tk.Frame(window, bg="#ADD8E6",highlightthickness=3,highlightcolor='#DC5539',padx=10,pady=10)
frame1.pack(padx=10,pady=0,side=LEFT)
frame1.place(x=40,y=200)
frame2 = tk.Frame(window, bg="#ADD8E6",padx=10,pady=10)#highlightthickness=3,highlightcolor='#DC5539'
frame2.pack(padx=10,pady=10,side=LEFT)
frame2.place(x=600,y=200)
# Creating buttons and entry fields
def Input_vector():
    #creating frames

    v1 = tk.Label(frame1, text="Enter vector 1: ", font=('calibre', 10, 'bold'), fg='#000000', bg='#ADD8E6')
    v1.grid(row=1,column=1,padx=20,pady=20)
    e1 = tk.Entry(frame1, width=30, justify=LEFT)
    e1.grid(row=1,column=2)
    v2 = tk.Label(frame1, text="Enter vector 2: ", font=('calibre', 10, 'bold'), fg='#000000', bg='#ADD8E6')
    v2.grid(row=3,column=1,padx=30,pady=20)
    e2 = tk.Entry(frame1, width=30, justify=LEFT)
    e2.grid(row=3,column=2)


myButton1 = tk.Button(window, text="Calculate", command=Input_vector(),font=('calibre', 10, 'bold'),
                      justify=LEFT,padx=10,pady=10
                      ,bg='#C1E1C1')
myButton2 = tk.Button(window, text="Run simulation",justify=RIGHT,bg='#C1E1C1',font=('calibre', 10, 'bold')
                      ,padx=5,pady=10)
myButton1.pack()
myButton2.pack()
myButton1.place(x=180, y=370)
myButton2.place(x=590, y=500)
"""label1 = tk.Label(frame2,
                  text="Vector info",
                  font=('Times new Roman', 10, 'bold'),
                  fg='#DC5539', bg='#000000',
                  )
label1.place(x=540, y=360)
label1.pack()"""


window.mainloop()

