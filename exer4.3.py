# leia um valor inteiro N que é a quantidade 
# de casos de teste que vem a seguir. Cada caso de teste 
# consiste de dois inteiros X e Y.
# Mostrar a soma de todos os ímpares entre X e Y.
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    soma = 0
    if x > y:
        for j in range(y + 1, x):
            if j % 2 != 0:
                soma += j
    else:
        for j in range(x + 1, y):
            if j % 2 != 0:
                soma += j
    print(soma)