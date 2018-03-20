#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

"""
    Questao 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus 
    colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

percentual = None
salario = float(input("Digite o salario do colaborador: "))

if salario <= 280.00 :
    percentual = 20
elif salario > 280.00 and salario <= 700.00 :
    percentual = 15
elif salario > 700.00 and salario < 1500.00 :
    percentual = 10
else :
    percentual = 5

reajuste =  (salario * percentual) / 100
salario_reajustado = salario + reajuste

print("\nSalario: R$ {:0.2f}".format(salario))
print("Perceltual de Aumento: {} %".format(percentual))
print("Valor do Aumento: R$ {:0.2f}".format(reajuste))
print("Salario com Aunmento: R$ {:0.2f}".format(salario_reajustado))
