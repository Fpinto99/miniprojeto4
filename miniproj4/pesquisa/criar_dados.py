import random

def criar_ficheiro_desordenado(nome_ficheiro,quantidade,max_valor):
    with open(nome_ficheiro,'w') as ficheiro:
        for _ in range(quantidade):
            num = random.randint(0,max_valor)
            ficheiro.write(str(num) + '\n')

def criar_ficheiro_ordenado(nome_ficheiro,quantidade,max_valor):
    with open(nome_ficheiro,'w') as ficheiro:
        nums = [random.randint(0,max_valor) for _ in range(quantidade)]
        nums.sort()
        for num in nums:
            ficheiro.write(str(num) + '\n')

quantidades = [100,1000,10000,100000,1000000]
max_valor = 1000000

for quantidade in quantidades:
    nome_ficheiro_desordenado = f'desordenado_{quantidade}.txt'
    nome_ficheiro_ordenado = f'ordenado_{quantidade}.txt'

    criar_ficheiro_desordenado(nome_ficheiro_desordenado,quantidade,max_valor)
    criar_ficheiro_ordenado(nome_ficheiro_ordenado,quantidade,max_valor)