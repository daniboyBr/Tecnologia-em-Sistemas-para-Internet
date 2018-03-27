#!/usr/bin/python3
# -*- coding: utf-8 -*

__author__ = "Daniel Evangelista Pereira"

"""
    Questao 07 - Faça um programa que leia 5 números e informe o maior número.
"""

maior = None
for i in range(1,6):
    num = float(input("Digite o {}º numero: ".format(i)))
    if i == 1:
        maior = num
    elif num > maior:
        maior = num
print("\nMaior numero: {}".format(maior))
