from tkinter import *

class Btn:
    def __init__(self, width = 20, bg='#ff0000', bg_name='red'):
        self.width = width
        self.bg = bg
        self.bg_name = bg_name
        btn = Button(width=self.width, bg = self.bg, command=self.magic)
        btn.pack()
    
    def magic(self):
        ent.delete(0, END)
        ent.insert(0, self.bg)
        lab['text'] = self.bg_name


root = Tk()

lab = Label(width=20, bg='black', fg='white', text='fsdfdfbht')
ent = Entry(width=20, justify='center')
spicoc_cvetov = [('#ff0000', 'красный'), ('#ff7d00', 'оранжевый'), ('#ffff00', 'желтый'), ('#00ff00', 'зелёный'), ('#007dff', 'голубой'), ('#0000ff', 'синий'), ('#7d00ff', 'фиолетовый'), ]

ent.pack()
for btn in spicoc_cvetov:
    Btn(bg=btn[0], bg_name=btn[1])
lab.pack()

root.mainloop()