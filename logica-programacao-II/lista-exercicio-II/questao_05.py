#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 05 - Faça um programa para a leitura de duas notas 
    parciais de um aluno. O programa deve calcular a média alcançada 
    por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = float(input("\nDigite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

media = (nota1 + nota2) / 2

print('\nMedia do Aluno: {:0.2f}'.format(media))
if media == 10.0:
    print("Aprovado com Distinção.")
elif media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")
