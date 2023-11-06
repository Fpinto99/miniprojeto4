from analise_dados import tempo
from analise_dados import boxplot
from analise_dados import complexidade
from analise_dados import complex_boxplot

tempo.f_tempo(tempo,100000,1000)
boxplot.f_boxplot([15,13,12,15,16,31,14,15,17,14,16,14,18,12,12,15,20,7])
complexidade.f_complexidade(complexidade,[15,13,12,15,16,31,14,15,17,14,16,14,18,12,12,15,20,7],1000)
complex_boxplot.f_complexidade_boxplot({'20': [34.54, 34.345, 34.761], '40': [34.541, 34.748, 34.482]})