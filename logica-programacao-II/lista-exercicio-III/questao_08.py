#!/usr/bin/python3
# -*- coding: utf-8 -*

__author__ = "Daniel Evangelista Pereira"

"""
    Questao 08 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma=0
for i in range(1,6):
    num = float(input("Digite o {}º numero: ".format(i)))
    soma += num 
print("Soma dos numeros: {}".format(soma))
print("\nMedia dos numeros: {:0.2f}".format(soma/5))
