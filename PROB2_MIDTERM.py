from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400")

def color():
 button.configure(bg="yellow")

button = Button(window, text = "Click to Change Color",font=("Calibri",10), command= color)
button.pack()
button.place(x=175,y= 180)

window.mainloop()