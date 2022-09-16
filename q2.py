class celula:
    def __init__(self,prox=None):
        self.n = input()
        self.i = int(input())
        self.a = float(input())
        self.p = prox
    def __str__(self):
        return 'Celula('+self.n+','+str(self.i)+','+str(self.a)+')'

n1 = celula()
print(n1)
n2 = celula(n1)
print(n2)
n3 = celula(n2)
print(n3)