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