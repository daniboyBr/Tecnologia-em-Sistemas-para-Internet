"""
    Questao 15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
    Faça um programa capaz de gerar a série até o n−ésimo termo
"""
anterior = 0
atual = 1

num_gerados = int(input("Digite a quantidade de numeros que deseja gerar: "))

if num_gerados > 0:
    for i in range(1,num_gerados+1):
        proximo = anterior + atual
        print(anterior)
        anterior = atual
        atual = proximo
else:
    print("\nNumero não pode ser 0 nem menor que Zero.")
