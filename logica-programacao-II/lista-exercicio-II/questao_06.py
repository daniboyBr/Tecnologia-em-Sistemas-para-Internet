#!/usr/bin/env python
# -*- coding: utf-8 -*

__author__="Daniel Evangelista Pereira"

#Questao 06 - Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("\nDigite um numero: "))
num2 = float(input("Digite um numero: "))
num3 = float(input("Digite um numero: "))

if num1 > num2 and num1 > num3 :
    print("\nPrimeiro numero digitado é o maior.")
elif num2 > num1 and num2 > num3 :
    print("\nSegundo numero digitado é o maior.")
else :
    print("\nTerceiro numero digitado é o maior")