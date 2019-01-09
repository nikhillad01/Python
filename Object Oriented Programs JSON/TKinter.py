import tkinter as tk
from tkinter import *
window=tk.Tk()
window.geometry("500x500")
window.title("Adress Book")

Label(window,text="First Name").grid(row=0)
Label(window,text="Last Name").grid(row=1)
Label(window,text="Address").grid(row=2)
Label(window,text="City").grid(row=3)
Label(window,text="State").grid(row=4)
Label(window,text="Zip").grid(row=5)
Label(window,text="Phone Number").grid(row=6)
e1=Entry(window).grid(row=0,column=1)
e2=Entry(window).grid(row=1,column=1)
e1=Entry(window).grid(row=2,column=1)
e2=Entry(window).grid(row=3,column=1)
e1=Entry(window).grid(row=4,column=1)
e2=Entry(window).grid(row=5,column=1)
e1=Entry(window).grid(row=6,column=1)

#window.resizable(0,0)
Button(window, text='Quit', command=window.quit).grid(row=7, column=0, sticky=W, pady=4)
Button(window, text='Submit').grid(row=7, column=1, sticky=W, pady=4)
window.mainloop()

#address, city, state, zip, and
#phone number.

