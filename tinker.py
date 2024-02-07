'''
import tkinter as t
x=t.Tk()
entry=t.Entry(x)
entry.pack()
def msg():
    print(entry.get())
    print('hello')
button=t.Button(x,text='print',command=msg)
button.pack()
x.mainloop()


import tkinter as t
x=t.Tk()
label=t.Label(x,text="m s p")
label.pack()
def mc():
    print("gui")
label.bind("<Button-1>",lambda e:mc())
x.mainloop()


from tkinter import messagebox as m
title="c s"
text="yy"
r=m.askquestion(title,text)
if r=='yes':
    print('s')
else:
    print('no')

import tkinter as t
x=t.Tk()
p=t.Toplevel()
p.title('t p w')
def des():
    p.destroy()
cb=t.Button(x,text='c w',command=des)
cb.pack()
x.mainloop()


import tkinter as t
x=t.Tk()
p=t.Toplevel()
p.title('t p w')
p.focus_force()
x.mainloop()
'''

import tkinter as t
x=t.Tk()
can=t.Canvas(x)
can.pack()
can.create_line(0,0,250,250,fill="orange",dash=(5,15))
can.create_rectangle(100,50,150,60,fill="yellow")
can.create_oval(30,30,50,50,fill="green")
x.mainloop()



















