"""
    Questao 39 - Faça um programa que leia dez conjuntos de dois valores, 
    o primeiro representando o número do aluno e o segundo 
    representando a sua altura em centímetros. Encontre o aluno 
    mais alto e o mais baixo. Mostre o número do aluno mais alto e 
    o número do aluno mais baixo, junto com suas alturas.
"""
aluno_mais_baixo = []
aluno_mais_alto = []
for i in range(1,11):
    num_aluno = int(input("Digite o numero do {}º aluno: ".format(i)))
    altura_aluno = float(input("Digite a altura do {}º aluno: ".format(i)))
    if i == 1:
        aluno_mais_alto.append(num_aluno)
        aluno_mais_alto.append(altura_aluno)
        aluno_mais_baixo.append(num_aluno)
        aluno_mais_baixo.append(altura_aluno)
    elif altura_aluno > aluno_mais_alto[1]:
        aluno_mais_alto[0] = num_aluno
        aluno_mais_alto[1] = altura_aluno
    elif altura_aluno < aluno_mais_baixo[1]:
        aluno_mais_baixo[0] = num_aluno
        aluno_mais_baixo[1] = altura_aluno
print("Aluno mais alto: numero {} Altura: {:0.2f}".format(aluno_mais_alto[0],aluno_mais_alto[1]))
print("Aluno mais baixo: numero {} Altura: {:0.2f}".format(aluno_mais_baixo[0],aluno_mais_baixo[1]))