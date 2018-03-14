#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

#Questao 04 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

media = 0
for i in range(1,5):
    media += float(input("Digite a Nota "+str(i)+": "))
print("Media do Aluno: {:0.2f}".format(media/4))