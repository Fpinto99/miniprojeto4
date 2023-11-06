import matplotlib.pyplot as plt

def f_boxplot(tempos_execucao):
    plt.boxplot(tempos_execucao)
    plt.xlabel('Execuções')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Boxplot de Tempos de Execução')
    plt.show()