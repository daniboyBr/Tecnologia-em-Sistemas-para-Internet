"""
    Questao 48 - Faça um programa que peça um numero inteiro positivo 
    e em seguida mostre este numero invertido.
"""

numeros = input("Digite um numero: ")
indice = len(numeros)
invertido = ""
for i in range(1,indice+1) :
    invertido += str(numeros[-i])
print(invertido)