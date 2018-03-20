#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 08 - Faça um programa que pergunte o preço de três produtos
    e informe qual produto você deve comprar, sabendo que a decisão é
    sempre pelo mais barato.
"""
mais_barato = None
for i in range(0,3) :
    produto = float(input("\nDigite um produto: "))
    if i == 0 :
        mais_barato = produto
    elif produto < mais_barato :
        mais_barato = produto
print("\nProduto mais barato custa: R$ {:0.2f}".format(mais_barato))
