# Escreva um programa que leia um valor inteiro N.
# N * 2 linha de saída serão apresentadas na execução do programa,
# seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos,
# todos os dígitos devem ser apresentados.
# Entrada
# O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).
# Saída
# Imprima a saída conforme o exemplo fornecido.

n = int(input())
for i in range(1, n + 1):
    print(i, i**2, i**3)
    print(i, i**2 + 1, i**3 + 1)