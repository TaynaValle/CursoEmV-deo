"""
Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre na tela quantos dólares ela pode
comprar

"""
dinheiro = float(input('Qual o valor em dinheiro você tem na carteira?'))
print('Você pode trocar o seu dinheiro por {:.2f} Dólares '.format(dinheiro / 4.11))