#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 03 - Faça um Programa que verifique se uma letra 
    digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, 
    M - Masculino, Sexo Inválido.
"""

sexo = input("\nDigite o sexo M(masculino) ou F(feminino): ")

if sexo.lower().strip() == "f":
    print("\nF - Feminino")
elif sexo.lower().strip() == "m":
    print("\nM - Masculino")
else:
    print("\nSexo inválido")