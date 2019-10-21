#Escreva um programa que leia um valor em metros e o exibha convertendo em centímetros e milímetros

metros = int(input('Metros:'))
c = metros * 100
m = metros * 1000
print('Convertendo {} em centímetro e milímetros, temos: {} centímetros e {} milímetros'.format(metros, c, m))