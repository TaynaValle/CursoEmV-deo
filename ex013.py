''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento '''

salário =float(input('Qual o valor salário do seu funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passou a receber R${:.2f}, '.format(salário, aumento))