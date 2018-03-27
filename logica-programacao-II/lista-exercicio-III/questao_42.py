"""
    Questao 42 - Faça um programa que leia uma quantidade indeterminada 
    de números positivos e conte quantos deles estão nos seguintes 
    intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados 
    deverá terminar quando for lido um número negativo.
"""

num = 0
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
while num >= 0 :
    num = int(input("\nDigite um numero inteiro positivo: "))
    if num >=0 and num <=25:
        intervalo1+=1
    elif num >= 26 and num <= 50:
        intervalo2+=1
    elif num >= 51 and num <= 75:
        intervalo3+=1
    else:
        if num > 0:
            intervalo4+=1
print("\nNumeros no intervalo de [0-25]: {}".format(intervalo1))
print("Numeros no intervalo de [26-50]: {}".format(intervalo2))
print("Numeros no intervalo de [51-75]: {}".format(intervalo3))
print("Numeros no intervalo de [76-100]: {}".format(intervalo4))