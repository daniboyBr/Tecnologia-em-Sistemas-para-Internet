#!/usr/bin/python3
# -*- coding: utf-8 -*
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 14 - Faça um programa que lê as duas notas parciais 
    obtidas por um aluno numa disciplina ao longo de um semestre, 
    e calcule a sua média. A atribuição de conceitos obedece à 
    tabela abaixo:

    O algoritmo deve mostrar na tela as notas, a média, o conceito 
    correspondente e a mensagem “APROVADO” se o conceito for A, B 
    ou C ou “REPROVADO” se o conceito for D ou E.
"""

aprovados = "abc"

nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

media = (nota1+nota2)/2

conceito = None
if media > 9.0 and media <= 10.0:
    conceito = "a"
elif media > 7.5 and media <= 9.0:
    conceito = "b"
elif media > 6.0 and media <= 7.5:
    conceito = "c"
elif media > 4.0 and media <= 6.00:
    conceito = "d"
else:
    conceito = "e"

print("\nNota 1: {:0.2f}".format(nota1))
print("Nota 2: {:0.2f}".format(nota2))
print("Conceito: {}".format(conceito.upper()))
print("Media: {:0.2f}".format(media))
print("APROVADO " if conceito in aprovados else "REPROVADO")
