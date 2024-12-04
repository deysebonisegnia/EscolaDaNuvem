# Escreva um programa  que leia dois valores X e Y.A seguir,mostre uma sequência
# de 1 até Y,passando para a próxima linha a cada X números.

x, y = map(int, input().split())
cont = 1
for i in range(1, y + 1):
    print(cont, end=" ")
    if i % x == 0:
        print()
    cont += 1