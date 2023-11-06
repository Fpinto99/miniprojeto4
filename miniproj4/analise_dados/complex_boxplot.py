import matplotlib.pyplot as plt
import statistics
def f_complexidade_boxplot(dic_tempos):
    lista_inputs = list(dic_tempos.keys())
    tempos_medios = [statistics.mean(dic_tempos[input]) for input in lista_inputs]

    plt.plot(lista_inputs, tempos_medios, marker='o')
    plt.xlabel('Inputs')
    plt.ylabel('Tempo Médio de Execução')
    plt.title('Tempo Médio de Execução em Função dos Inputs')
    plt.show()