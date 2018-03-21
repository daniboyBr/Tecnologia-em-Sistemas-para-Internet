#!/usr/bin/python3
# -*- coding: utf-8 -*
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 15 -  Faça um Programa que peça os 3 lados de um triângulo. 
    O programa deverá informar se os valores podem ser um triângulo. 
    Indique, caso os lados formem um triângulo, se o mesmo é: 
    equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois 
    lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""
lados = []
for i in range(0,3):
    lado = float(input("Digite o lado {}: ".format(i+1)))
    lados.append(lado)

condicao1 = lados[1]-lados[2] < lados[0] < lados[1]+lados[2]
condicao2 = lados[0]-lados[2] < lados[1] < lados[0]+lados[2]
condicao3 = lados[0]-lados[1] < lados[2] < lados[0]+lados[1]

if condicao1 and condicao2 and condicao3:
    print("\nPode ser um triangulo.")
    if lados[0] == lados[1] and lados[1] == lados[2]:
        print("Triangulo Equilatero")
    elif lados[0] == lados[1] or lados[1] == lados[2] or lados[2] == lados[0]:
        print("Triangulo Isóceles")
    else:
        print("Triangulo Escaleno")
else:
    print("\nValore digitados não formam um triangulo.")
        




