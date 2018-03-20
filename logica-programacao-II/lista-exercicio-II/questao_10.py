#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 10 - Faça um Programa que pergunte em que turno você estuda. 
    Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima 
    a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
    "Valor Inválido!", conforme o caso.
"""
turno = {
    'm':"Bom Dia!",
    'v':"Bom Tarde!",
    'n':"Bom Noite!"
}

turno_informado = input("\nTurno:\n\tM-matutino\n\tV-Vespertino\n\tN-Noturno\nDigite o turno em que estuda: ")
turno_informado = turno_informado.lower().strip()
if turno_informado in turno :
    print("\n"+turno[turno_informado])
else :
    print("\nValor Invalido!")
