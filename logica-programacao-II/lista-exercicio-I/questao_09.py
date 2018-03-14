#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 09 - Faça um Programa que peça a temperatura em graus Farenheit, 
    transforme e mostre a temperatura em graus Celsius.
    Obs: formula para conversão: C = (5 * (F-32) / 9).
"""

farenheit = float(input("Digite a temperatura em Farenheit: "))
celsius = (5*(farenheit-32)/9)
print("Temperatura em graus Celsius: {:0.2f}".format(celsius))