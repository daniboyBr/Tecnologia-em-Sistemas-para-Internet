#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

# Questao 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []
for i in range(0,3) :
    num = float(input("\nDigite um numero: "))
    numeros.append(num)
numeros = sorted(numeros,reverse=True)
for i in range(0,3) :
    print(numeros[i])
