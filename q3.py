Retornar o último No da Arvore Binaria

class celula:
    def __init__(self, valor, FE=None, FD=None, visitado= False, alturaNo=0):
        self.valor = valor
        self.fe = FE
        self.fd = FD    
        self.visitado = visitado
        self.alturaNo = alturaNo
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
    

    
def ultimoNo(arvore):
    altura = 0
    atual = arvore
    pilha: List[celulas] = [None]
    ultimoNo = arvore
                                                     
    while (atual != None):
        if(atual.alturaNo > ultimoNo.alturaNo):
            ultimoNo = atual
        elif(atual.fe != None and atual.fe.visitado == False):
            pilha.append(atual)
            atual = atual.fe
            altura += 1
            atual.alturaNo = altura            
        elif(atual.fd != None and atual.fd.visitado == False):
            pilha.append(atual)
            atual = atual.fd
            altura += 1
            atual.alturaNo = altura            
        else:
            atual.visitado = True
            altura -=1
            atual = pilha.pop()
    
    return ultimoNo

  


r = celula(7)
n1 = celula(3)
n2 = celula(1)
n3 = celula(4)
n4 = celula(11)
n4.fd=celula(15)

r.fe = n1
n1.fe = n2
n1.fd = n3
r.fd = n4

p = ultimoNo(r)
print(p)