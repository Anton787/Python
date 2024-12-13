class Table1:
    def __init__(self):
        self.n = 20
    
    def total(self, a):
        return self.n + int(a)
    
class Table2:
    def __init__(self):
        self.text = 'hello'
    
    def total(self, a):
        return len(self.text + str(a))
    
t1 = Table1()
t2 = Table2()

print(t1.total(35))
print(t2.total(35))

class G:
    def __init__(self, v1, v2):
        self.f1 = v1
        self.f2 = v2
    
    def __str__(self):
        s = ''
        for i in range(self.f1):
            for j in range(self.f2):
                s += '* '
        s += '\n'
        return s

a = G(3, 4)
b = str(a)
print(a)
print(b)