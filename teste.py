class no:
    def __init__(self,valor):
        self.valor=valor
        self.fe=None
        self.fd=None

    def __str__(self):
        return 'No('+str(self.valor)+')'

def ultimoNo(arvore):
    atual = arvore

    while(atual.valor != None):
        if (atual.fe != None):
            atual = atual.fe
        elif (atual.fd != None):
            atual = atual.fd
        else:
            break

    return print(atual)


raiz = no(4)
raiz.fe = no(3)
raiz.fe.fe = no(2)
raiz.fe.fe.fe = no(1)
ultimoNo(raiz)