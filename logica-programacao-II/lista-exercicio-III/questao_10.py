"""
    Questao 10 - Faça um programa que receba dois números inteiros e 
    gere os números inteiros que estão no intervalo compreendido por eles.
"""

inicio = int(input("Digite o inicio do intervalo: "))
final = int(input("Final do intervalo: "))

if inicio > final:
     print("\nInicio do intervalo nao pode ser maior que o final.")
else:
    for i in range(inicio,final+1):
        print("\n{}".format(i))