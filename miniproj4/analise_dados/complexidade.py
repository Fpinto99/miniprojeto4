from .tempo import f_tempo

def f_complexidade(funcao, lista_inputs, n_vezes):
    dic_stats = {}
    dic_tempos = {}
    print(lista_inputs[0])

    for input in lista_inputs:
        tempos_execucao, tempo_medio, desvio_padrao = f_tempo(funcao, input, n_vezes)
        dic_stats[input] = (tempo_medio, desvio_padrao)
        dic_tempos[input] = tempos_execucao

    return dic_stats, dic_tempos