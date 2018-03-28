"""
    Questao 36 - Desenvolva um programa que faça a tabuada 
    de um número qualquer inteiro que será digitado pelo 
    usuário, mas a tabuada não deve necessariamente iniciar 
    em 1 e terminar em 10, o valor inicial e final devem ser 
    informados também pelo usuário, conforme exemplo abaixo:
"""

num = int(input("Montar tabuada de: "))
inicio = 0 
final = 0 
while True:
    inicio = int(input("\nComecar por: "))
    final = int(input("Terminar em: "))
    if inicio < final: 
       break
    else:
        print("\nO numero de inicio deve ser menor que o numero final. Digite novamente.")

print("\nVou montar a tabuada de {} começando em {} e terminando em {}: ".format(num,inicio,final))
for i in range(inicio, final+1):
    print("{} x {} = {}".format(num, i, num * i))
