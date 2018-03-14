#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 07 - Faça um Programa que calcule a área de um quadrado, 
    em seguida mostre o dobro desta área para o usuário.
"""

lado = float(input("Digite o lado do Quadrado: "))
area = lado**2
print("Dobro da área do quadrado: {:0.2f}".format(area*2))