#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 13 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
    o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    
        a)salário bruto.
        b)quanto pagou ao INSS.
        c)quanto pagou ao sindicato.
        d)o salário líquido.
        e)calcule os descontos e o salário líquido
        Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

horas_trabalhadas = int(input("Informe a quantidade de Horas trabalhadas: "))
valor_hora = float(input("Informe o valor por hora trabalhada: "))

salario_bruto = horas_trabalhadas * valor_hora
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sidicato = (salario_bruto * 5) / 100

print("\n+ Salário Bruto: R$ {:0.2f}".format(salario_bruto))
print("- IR (11%): R$ {:0.2f}".format(ir))
print("- INSS (8%): R$ {:0.2f}".format(inss))
print("- Sindicato (5%): {:0.2f}".format(sidicato))
print("+ Salário Líquido: R$ {:0.2f}\n".format(salario_bruto-(ir+inss+sidicato)))
