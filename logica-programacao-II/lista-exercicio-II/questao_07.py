#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

# Questao 07 - Faça um Programa que leia três números e mostre o maior e o menor deles.

maior = None
menor = None
for i in range(0,3) :
    num = float(input("Digite um numero: "))
    if i == 0:
        maior = num
        menor = num
    elif num >= maior :
        maior = num
    elif num <= menor:
        menor = num
print("Maior numero digitado: {}".format(maior))
print("Menor numero digitado: {}".format(menor))
            
