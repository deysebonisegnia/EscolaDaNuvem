# Escreva um programa que leia 2 valores
# x e y e que imprima todos os valores entre 
#eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.
x = int(input())
y = int(input())
if x > y:
    for i in range(y + 1, x):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
else:
    for i in range(x + 1, y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)