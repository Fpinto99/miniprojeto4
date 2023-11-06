import time
import statistics

def f_tempo(pesquisa_sequencial, input, n_vezes):
    tempos_execucao = []
    for _ in range(n_vezes):
        inicio = time.time()
        pesquisa_sequencial(input)
        fim = time.time()
        tempos_execucao.append(fim - inicio)

    tempo_medio = statistics.mean(tempos_execucao)

    print(tempos_execucao, tempo_medio)



def f_tempo1(pesquisa, input, n_vezes):
    tempos_execucao = []
    for _ in range(n_vezes):
        inicio = time.time()
        pesquisa(input)
        fim = time.time()
        tempos_execucao.append(fim - inicio)

    tempo_medio = statistics.mean(tempos_execucao)

    print(tempos_execucao, tempo_medio)

def f_tempo2(pesquisa_sequencial_lista_ordenada, input, n_vezes):
    tempos_execucao = []
    for _ in range(n_vezes):
        inicio = time.time()
        pesquisa_sequencial_lista_ordenada(input)
        fim = time.time()
        tempos_execucao.append(fim - inicio)

    tempo_medio = statistics.mean(tempos_execucao)

    print(tempos_execucao, tempo_medio)

def f_tempo3 (pesquisa_binaria, input, n_vezes):
    tempos_execucao = []
    for _ in range(n_vezes):
        inicio = time.time()
        pesquisa_binaria(input)
        fim = time.time()
        tempos_execucao.append(fim - inicio)

    tempo_medio = statistics.mean(tempos_execucao)

    print(tempos_execucao, tempo_medio)

def f_tempo4 (pesquisa_binaria2, input, n_vezes):
    tempos_execucao = []
    for _ in range(n_vezes):
        inicio = time.time()
        pesquisa_binaria2(input)
        fim = time.time()
        tempos_execucao.append(fim - inicio)

    tempo_medio = statistics.mean(tempos_execucao)

    print(tempos_execucao, tempo_medio)