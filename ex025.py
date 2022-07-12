##Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite seu nome completo: '))
nome_lista = nome.split()
resultado = 'Silva' in nome_lista
print(resultado)
