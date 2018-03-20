#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 12 - Faça um programa para o cálculo de uma folha de pagamento, 
    sabendo que os descontos são do Imposto de Renda, que depende do salário 
    bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS 
    corresponde a 11% do Salário Bruto, mas não é descontado 
    (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
    menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
    e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
    dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a 
    quantidade de hora é 220. 
"""

valor_hora =  float(input("\nDigite o valor por hora trabalhada: "))
horas_trabalhada = int(input("Digite o total de horas trabalhadas: "))
salario_bruto = valor_hora * horas_trabalhada

percentual_desconto = None
if salario_bruto > 900 and salario_bruto <=1500:
    percentual_desconto = 5
elif salario_bruto > 1500 and salario_bruto <= 2500 :
    percentual_desconto = 10
else:
    percentual_desconto = 20

ir = (salario_bruto*percentual_desconto)/100
fgts = (salario_bruto*11)/100
inss = (salario_bruto*10)/100
total_descontos = ir + inss

print("\nSalario Bruto            : R$ {:0.2f}".format(salario_bruto))
print("(-) IR                   : R$ {:0.2f}".format(ir))
print("(-) INSS                 : R$ {:0.2f}".format(inss))
print("FGTS                     : R$ {:0.2f}".format(fgts))
print("Total de Descontos       : R$ {:0.2f}".format(total_descontos))
print("Salario Liquido          : R$ {:0.2f}".format(salario_bruto-total_descontos))