#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    transforme e mostre em graus Farenheit.
    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.
"""

num1_int = int(input("Digite um numero inteiro: "))
num2_int = int(input("Digite outro numero inteiro: "))
num3_flo = float(input("Digite um numero real: "))

print("O produto do dobro do primeiro com metade do segundo: ",(num1_int*2)*(num2_int/2))
print("A soma do triplo do primeiro com o terceiro: ",(num1_int*3 + num3_flo))
print("O terceiro elevado ao cubo: ",num3_flo**3)