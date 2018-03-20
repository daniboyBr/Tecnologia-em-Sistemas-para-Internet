#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 13 - Faça um Programa que leia um número e exiba 
    o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
    se digitar outro valor deve aparecer valor inválido. 
"""
dias = {
    1:"Domingo",
    2:"Segunda",
    3:"Terça",
    4:"Quarta",
    5:"Quinta",
    6:"Sexta",
    7:"Sábado"
}

dia_informado = int(input("\nDias da Semana: \
\n1 - Domingo\
\n2 - Segunda\
\n3 - Terça\
\n4 - Quarta\
\n5 - Quinta\
\n6 - Sexta\
\n7 - Sábado\
\nDigite um numero: "))

if dia_informado in dias:
    print(dias[dia_informado])
else:
    print("\nValor digitado invalido.")