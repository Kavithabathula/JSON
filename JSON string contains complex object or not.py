# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

# import json
# def fun(objct):
#     if 'complex' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# x =json.loads('{"complex": true, "real": 4, "img": 3}', object_hook = fun)
# y =json.loads('{"real": 4, "img": 3}', object_hook =fun)
# print("Complex object: ",x)
# print("Without complex object: ",y)



import tkinter
from tkinter import *
from tkinter import messagebox

root=tkinter.Tk()
root.title("demo")
root.geometry("600x600")

'''# label
label=tkinter.Label(root,text="Hai I am Kavita").pack()

# Button
b=Button(root,text="Hello Python",bg="blue",fg="pink")
b.grid(column=1,row=0)

# radio
r=Radiobutton(root,text="Python",value=1)
r.grid(column=2,row=1)
r1=Radiobutton(root,text="c",value=1)
r1.grid(column=2,row=2)
r2=Radiobutton(root,text="c++",value=1)
r2.grid(column=2,row=3)

#entry
t=Entry(root,width=100)
t.grid(column=3,row=0)'''

#message
def Button1():
    messagebox.showinfo("status","Study well about Python")
b=Button(root,text="Python life",command=Button1)
b.pack()

root.mainloop()