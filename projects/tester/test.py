#how to create simple GUI registration form.
#importing tkinter module for GUI application
from tkinter import Tk, Spinbox
from tkinter.ttk import Style, Label, Button, Combobox

#Creating object 'root' of Tk()
top = Tk()
Style().configure('TButton', forground = 'white', background = 'red')

Label(top, text = 'Animals (in pairs; min: pair, max: dozen)').pack()
Label(top, text = 'Number').pack()

Spinbox(top, from_=2, to=12, increment=2, font='Helvetica -14 bold').pack()

Label(top, text='Type').pack()

Combobox(top, values=('dog', 'cat', 'hamster', 'python')).pack()

Button(top, text='QUIT', command=top.quit, style='TButton').pack()

#this will run the mainloop.
top.mainloop()