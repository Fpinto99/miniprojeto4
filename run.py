from analise_dados.tempo import f_tempo
from analise_dados.complexidade import f_complexidade
import matplotlib.pyplot as plt

def pesquisa_sequencial(lista, item):
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
    return encontrado

n_values = [1000000, 100, 1000, 10000]
tempos_execucao = []

for n in n_values:
    tempos_execucao_n, _, _ = f_tempo(pesquisa_sequencial(n_values,0), n, 1000)
    tempos_execucao.append(tempos_execucao_n)

dic_stats, _ = f_complexidade(pesquisa_sequencial([],0), n_values, 1000)

lista_inputs = list(dic_stats.keys())
tempos_medios = [dic_stats[n][0] for n in n_values]

plt.plot(n_values, tempos_medios, marker='o')
plt.xlabel('n')
plt.ylabel('Tempo Médio de Execução (s)')
plt.title('Complexidade da Função Soma de Inteiros')
plt.show()