from functools import partial as pto
from tkinter import Button, Tk, X
from tkinter.constants import HORIZONTAL
from tkinter.messagebox import showinfo, showerror

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())



top = tkinter.Tk()
top.geometry('250x150')
label = tkinter.Label(top, text = 'Hello World!', font='Helvetica -12 bold')
label.pack()

font_minSize = 10
font_MaxSize = 50
scale = tkinter.Scale(top, from_=font_minSize, to=font_MaxSize, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tkinter.X, expand=1)

quit = tkinter.Button(top, text='QUIT', command=top.quit, bg='yellow', fg='blue')
quit.pack()

tkinter.mainloop()