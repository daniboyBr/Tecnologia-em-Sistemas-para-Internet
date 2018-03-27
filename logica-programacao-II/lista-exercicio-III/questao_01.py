#!/usr/bin/python3
# -*- coding: utf-8 -*

__author__ = "Daniel Evangelista Pereira"

"""
    Questao 01 - Faça um programa que peça uma nota, entre zero e dez. 
    Mostre uma mensagem caso o valor seja inválido e continue pedindo 
    até que o usuário informe um valor válido.
"""

num = -1
while num not in range(0,11):
    num  = float(input("\nDigite um numero: "))
    condicao = "\nNumero invalido. Tente novamente." if num < 0 or num > 10 else "\nNumero valido!"
    print(condicao)