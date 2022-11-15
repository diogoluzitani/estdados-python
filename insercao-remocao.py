from sre_constants import SUCCESS


class celula:
    def __init__(self, valor, FE=None, FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD    
        
    def __str__(self):
        return "No("+str(self.valor)+")"

class arvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def buscaPai(self, valor):
        aux2 = None
        aux = self.raiz
        while (aux!= None):
            aux2 = aux
            if(valor < aux.valor):
                aux = aux.fe
            elif (valor > aux.valor):
                aux = aux.fd
        return aux2


#INSERCAO
#Encontrar pai
#conectar o pai com o novo no
    def insercao(self, valor):
        novo = celula(valor)

        if(self.raiz == None):
            self.raiz = novo
        else:
            pai = self.buscaPai(valor)
            if(valor<pai.valor):
                pai.fe = novo
            else: 
                pai.fd = novo

#REMOÇÃO:
#Encontrar o nó sucessor e o seu pai
    def sucessor(self, no):
        suc = no.fd
        pai = None
        while(suc != None):
            if(suc.fe == None):
                break
            pai = suc
            suc = suc.fe
        return suc, pai

#Encontrar o nó antecessor e o seu pai
    def antecessor(self, no):
        ant = no.fe
        pai = None
        while(ant != None):
            if(ant.fd == None):
                break
            pai = ant
            ant = ant.fd
        return ant, pai

#Substituir o nó Sucessor com o nó a ser removido
    def trocaValor(self, no1, no2):
        temp = no1.valor
        no1.valor = no2.valor
        no2.valor = temp

# verificar se podemos Remover o nó ou conectar seu filho o Pai do Sucessor
    def remocao(self, rem):
        prox, pai = self.sucessor(rem)
        if(succ == None):
            prox, pai = self.antecessor(rem)
        self.trocaValor(rem, prox)
        if(prox.fd == None):
            pai.fe = None
        else:
            pai.fe = prox.fd


abb = arvoreBinaria()
abb.insercao(10)
abb.insercao(17)
abb.insercao(5)

print(abb.raiz)
print(abb.raiz.fd)
print(abb.raiz.fe)

rem = abb.raiz
succ, pai = abb.sucessor(rem)

abb.trocaValor(rem, succ)


        



    





