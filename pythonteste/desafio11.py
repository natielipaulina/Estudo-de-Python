largura = float(input('Qual é a largura da parede?'))
altura = float(input('Qual é a altura da parede?'))
área = largura * altura
litros_tinta = área/2
print('A área da parede é {:.2f} m²'.format(área))
print('A quantidade de tinta necessária para pintá-la é {:.2} litros'.format(litros_tinta))