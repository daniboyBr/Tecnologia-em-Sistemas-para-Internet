"""
    Questao 19 - Faça um programa que, dado um conjunto de 
    N números, determine o menor valor, o maior valor e 
    a soma dos valores.
"""

num = int(input("Digite quantidade de numeros que deseja informar: "))
maior = 0
menor = 0 
soma = 0 
for i in range(1,num+1):
    numero = float(input("Digite um valor: "))
    if i == 1:
        maior = numero 
        menor = numero
    elif numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
    soma += numero
print("\n\nSoma dos valores digitados: {:0.2f}".format(soma))
print("Maior valor digitado: {:0.2f}".format(maior))
print("Menor valor digitado: {:0.2f}".format(menor))
