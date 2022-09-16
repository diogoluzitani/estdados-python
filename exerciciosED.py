class celula:
    def __init__(self, valor, FE=None, FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD    
        
    def __str__(self):
        return "No("+str(self.valor)+")"

def busca(r, nova):
    atual = r
                
    while (atual.valor != None):
        if (nova < atual.valor) and (atual.fe != None):
                atual = atual.fe
        elif(nova > atual.valor) and (atual.fd != None):
                atual = atual.fd
        else:
            return "No("+str(atual.valor)+")"


r = celula(7)
n1 = celula(3)
n2 = celula(1)
n3 = celula(4)
n4 = celula(11)

r.fe = n1
n1.fe = n2
n1.fd = n3
r.fd = n4

nova = celula(int(input()))

p = busca(r, nova.valor)

print(p)

------

class celula:
    def __init__(self, valor, FE=None, FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD    
        
    def __str__(self):
        return "No("+str(self.valor)+")"

def busca(r, nova):
    atual = r
                
    while (atual.valor != None):
        if (nova < atual.valor) and (atual.fe != None):
                atual = atual.fe
        elif(nova > atual.valor) and (atual.fd != None):
                atual = atual.fd
        else:
            return atual

def inserir(r, valor):
    pai = busca(r, valor)
    
    if(valor > pai.valor):
        pai.fd=celula(valor)
    else:
        pai.fe=celula(valor)
    
    return pai


r = celula(7)
n1 = celula(3)
n2 = celula(1)
n3 = celula(4)
n4 = celula(11)

r.fe = n1
n1.fe = n2
n1.fd = n3
r.fd = n4

nova = celula(int(input()))

p = inserir(r, nova.valor)
