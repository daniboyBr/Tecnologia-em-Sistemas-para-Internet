#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 08 - Faça um Programa que pergunte quanto você ganha por hora e o número de 
    horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

horas_trabalhadas = int(input("Digite as horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor por hora: "))
salario_mes = horas_trabalhadas*valor_hora
print("Salário do mês: R$ {:0.2f}".format(salario_mes))