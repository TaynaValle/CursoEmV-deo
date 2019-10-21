# Faça um programa que leia um número inteiro e mostre na tela o seu sussesor e seu antessesor

n = int(input('Digite um número:'))
su = n + 1
an = n - 1
print('Seu sussessor é {} e o seu antessessor é {}'.format(su, an))
