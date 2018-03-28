"""
    Questao 14 - Faça um programa que peça 10 números inteiros, 
    calcule e mostre a quantidade de números pares e a 
    quantidade de números impares.
"""
impares=0
pares=0
i = 1
while i <= 10:
    num = int(input("Digite um numero: "))
    if num % 2 == 0 :
        pares+=1
    else:
        impares+=1
    i+=1
print("Quantidade de numeros impares: {}".format(impares))
print("Quantidade de numeros impares: {}".format(pares))

    
