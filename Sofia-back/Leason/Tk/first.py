from tkinter import *
from random import choice

def click(e):
    # btn['text'] = choice(['text1', 'banana', 'hello', 'click'])
    a = ent.get()
    print(a)

root = Tk()

ent = Entry(width=20)
btn = Button(text='Ok', command=lambda: print('123'))
lab = Label(width=20, bg='none', fg='black', text='dasdasdasdasda')

btn.bind('<Button-1>', click)

ent.pack()
btn.pack()
lab.pack()

root.mainloop()

