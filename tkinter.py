#import sys
import tkinter as t
x=t.Tk()
'''
#print(tkinter.TkVersion)
x.title('voter id registration form')
x.mainloop()

w=x.winfo_screenwidth()
h=x.winfo_screenheight()
print(w,h)

x.attributes('-fullscreen',True)
x.mainloop()


#x.geometry('900x200+200+200')

msg=t.Label(x,text=' Apply voter id',background='yellow')
msg1=t.Label(x,text='u should be indian',background='green')
msg.config(font=("callibri",28,"italic bold underline"))
msg.pack(fill=t.Y,padx=10,ipady=25,side=t.RIGHT)
msg1.pack(fill=t.Y,padx=20,ipady=40,side=t.RIGHT)
x.mainloop()

img=t.PhotoImage(file=sys.argv[1])
IMG=t.Lable(x,image=img)
IMG.pack()
x.mainloop()

exi=t.Button(x,text='close',command=x.destroy)
def show():
    print('u entered into 5d space')
msg=t.Button(x,text='click here',command=show)
msg.pack()
exi.pack()
x.mainloop()

msg=t.Label(x,text=' Apply voter id',background='yellow',foreground='red')
msg.pack()
x.mainloop()
'''
menu=t.Menu(x)
m=Menu(menu,tearoff=0)
m.add_command(label="stop",command=x.destroy)
x.mainloop()





