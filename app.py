class Celula:
    def __init__(self, nome, idade, altura, prox=None) -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.prox = prox

    def __str__(self):
        return 'Celula('+str(self.nome)+', '+str(self.idade)+', '+str(self.altura) +')'


n1=Celula(input(), int(input()), float(input()))
n2=Celula(input(), int(input()), float(input()))
n1.prox = n2
n3=Celula(input(), int(input()), float(input()), n2)
n2.prox = n3

