a = input('Digite algo:').strip()  # Remove espaços no início e no final

# Exibe o tipo primitivo da entrada
print('O tipo primitivo desse valor é', type(a))

# Verifica se contém apenas espaços
print('Só tem espaços?', a.isspace())

# Verifica se é um número
print('É um número?', a.isnumeric())

# Verifica se é composto apenas por letras
print('É alfabético?', a.isalpha())

# Verifica se é alfanumérico (letras e números)
print('É alfanumérico?', a.isalnum())

print('Está em maiúsculas?', a.isupper())

print('Está em minúsculas?', a.islower())

print('Está capitalizada?', a.istitle())