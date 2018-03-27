#!/usr/bin/python3
# -*- coding: utf-8 -*

__author__ = "Daniel Evangelista Pereira"

"""
    Questao 02 - Faça um programa que leia um nome de usuário 
    e a sua senha e não aceite a senha igual ao nome do 
    usuário, mostrando uma mensagem de erro e voltando a 
    pedir as informações.
"""

login = False
while login == False:
    user = input("\nDigite o nome de usuario: ")
    senha = input("Digite a senha: ")
    if user.strip() != senha.strip():
        print("\nUsuario e senha aceitos")
        login = True
    else:
        print("\nErro! Usuario e Senha nao pode ser iguais")

