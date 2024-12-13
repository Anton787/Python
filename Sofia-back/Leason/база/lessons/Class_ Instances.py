class Orange:
    def __init__(self, color = 'orange'): #Вызывается сразу при инициализации и благодоря этому не будут экземляры сразу индивидумальны 
        self.color = color
        
    def __del__(self):
        print('Апельсин умер x_X')

or1 = Orange('redorange')

del or1

# print(or1.color) Не будет так умер :(

