preço = float(input('Qual o preço do produto? R$'))
desconto = preço * 0.05
preço_com_desconto = preço - desconto
print('O preço original é {}'.format(preço))
print('O desconto do produto é {}'.format(desconto))
print('O preço com desconto é {}'.format(preço_com_desconto))