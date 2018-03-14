#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

#Questao 06 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o raio do Círculo: "))
area = 3.14 * (raio**2)
print("Área do Círculo: {:0.2f}".format(area))