#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Daniel Evangelista Pereira"

"""
    Questao 14 - Faça um programa que peça o tamanho de um arquivo para download (em MB) 
    e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
    de download do arquivo usando este link (em minutos).
"""

arquivo = int(input("Inseria o tamanho em (MB) do arquvio a ser baixado: "))
velocidade_link = int(input("Insira a velocidade do link em Mbps: "))

"""
    velocidade_link em Mbps multiplico por 60 para saber quantos Mb eu tenho em 1 minuto
    tendo a quantidade divido por 8 pois 1 MB = 8 Mb logo saberei quantos megas eu
    tenho em 1 minuto, ai divido o tarmanho do arquivo pela quantidade de megas que tenho em 
    1 minuto ai saberei quantos minutos vai durar.
"""
tempo_download = arquivo / ((velocidade_link*60)/8)
if tempo_download < 1:
    print("O tempo de download será: {:0.0f} segundos".format(tempo_download*60))
else:
    print("O tempo de download será: {:0.0f} minutos".format(tempo_download))
