#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 12 - Tendo como dados de entrada a altura de uma pessoa, 
    construa um algoritmo que calcule seu peso ideal, 
    usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = float(input("Informe a sua altura: "))
peso_ideal = (72.7*altura)-58
print("Peso ideal com base na sua altura: {:0.2f}".format(peso_ideal))