#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 10 - Faça um Programa que peça a temperatura em graus Celsius, 
    transforme e mostre em graus Farenheit.
"""

celsius = float(input("Digite a temperatura em Celsius: "))
farenheit = 1.8 * celsius + 32
print("Temperatura em Farenheit: {:0.2f}".format(farenheit))