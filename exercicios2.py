

Considerando a Classe TabelaHash implementada na video aula, implemente a função de mapeamento pelo método da divisão.

Considere que o usuário irá inserir 5 valores (um por vez) e seu programa deve imprimir a tabela com os valores preenchidos. O tamanho da Tabela dever ser 7.

Para isso, inclua a função input para ler os 5 valores de entradas. Após a leitura imprima a tabela resultante.
class TabelaHash:
    def __init__(self, M, codigo=-1):
        self.codigo = codigo
        self.tabela = [self.codigo]*M
        
    def hashFun(self, chave):
        pos = chave%7
        return pos
    
    def inserir(self, chave):
        pos = self.hashFun(chave)
        if self.tabela[pos] == self.codigo:
            self.tabela[pos] = chave
        else:
            return pos
    
    def buscar(self, chave):
        pos = self.hashFun(chave)
        if self.tabela[pos] == chave:
            print("Encontrado na posição", pos)
        else:
            print("Não encontrado")

t = TabelaHash(7)
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
print(t.tabela)

Considerando o exercício sobre a implementação da tabela de dispersão, considere agora mostrar a quantidade de colisões ocorridas.

Por exemplo, a inserção dos 4 valores 1,1,1,1 na tabela com 7 posições ocasionaria 3 colisões após a inserção do primeiro valor 1.

Por exemplo:


class TabelaHash:
    def __init__(self, M, codigo=-1, contador=0):
        self.codigo = codigo
        self.tabela = [self.codigo]*M
        self.contador = contador
        
    def hashFun(self, chave):
        pos = chave%7
        return pos
    
    def inserir(self, chave):
        pos = self.hashFun(chave)
        if self.tabela[pos] == self.codigo:
            self.tabela[pos] = chave
        else:
            self.contador += 1
    
    def buscar(self, chave):
        pos = self.hashFun(chave)
        if self.tabela[pos] == chave:
            print("Encontrado na posição", pos)
        else:
            print("Não encontrado")

t = TabelaHash(7)
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
print("Quantidade de Colisões:", t.contador)

Considerando nossa classe TabelaHash, implemente uma função de tratamento de colisão considerando o Hash Linear. Portanto, as inserções devem tratar essa colisões e a função de hash linear sugerir as novas posições.

Considere que o usuária irá informar 6 valores (um por vez) e a tabela tem tamanho 7. Em seguida, imprima a tabela.

Por exemplo:

Entrada	Resultado
7


3
1
14
5
0
7
3
1
14
5
0
[7, 1, 14, 3, 0, 5, -1]

class TabelaHash:
    def __init__(self, M, codigo=-1, contador=0):
        self.codigo = codigo
        self.tabela = [self.codigo]*M
        self.contador = contador
        
    def hashFun(self, chave):
        pos = chave%7
        return pos
    
    def inserir(self, chave, i=0):
        pos = self.hashFun(chave)
        if self.tabela[pos] == self.codigo:
            self.tabela[pos] = chave-i
        else:
            i += 1
            self.inserir(chave+1, i)
    
    def buscar(self, chave):
        pos = self.hashFun(chave)
        if self.tabela[pos] == chave:
            print("Encontrado na posição", pos)
        else:
            print("Não encontrado")

t = TabelaHash(7)
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
print(t.tabela)


class celula:
    def __init__(self, valor, FE=None, FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD    
        
    def __str__(self):
        return "No("+str(self.valor)+")"


        
r = celula(7)
n1 = int(3)
n2 = int(11)

r.fe = n1
r.fd = n2

print(r)
print(r.fe)
print(r.fd)

class celula:
    def __init__(self, valor, FE=None, FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD    
        
    def __str__(self):
        return "No("+str(self.valor)+")"


        
r = celula(int(input()))
n1 = celula(int(input()))
n2 = celula(int(input()))

r.fe = n1
r.fd = n2
