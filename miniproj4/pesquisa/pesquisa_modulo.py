def pesquisa_sequencial(lista, item):
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
    return encontrado

def pesquisa_sequencial_lista_ordenada(lista, item):
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
        if elemento > item:
            encontrado = False
            break
        return encontrado

def pesquisa(lista, n):
    if lista[0] == n:
        return True
    if len(lista) == 1:
        return False
    return pesquisa(lista[1:], n)

def pesquisa_binaria(lista, item):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro<=ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == item:
            return True

        else:
            if item < lista[meio]:
                ultimo = meio-1
            else:
                primeiro = meio+1
        return False

def pesquisa_binaria2(lista, item):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista)//2
        if lista[meio]==item:
            return True
        else:
            if item<lista[meio]:
                return pesquisa_binaria2(lista[:meio],item)
            else:
                return pesquisa_binaria2(lista[meio+1:],item)