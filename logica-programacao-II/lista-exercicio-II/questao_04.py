#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 04 - Faça um Programa que verifique se uma 
    letra digitada é vogal ou consoante.
"""

vogais = "aeiou"
letra = input("\nDigite uma letra: ")

if letra.lower().strip() in vogais :
    print("\nLetra digitada é vogal.")
else :
    print("\nLetra digitada é consoante.")