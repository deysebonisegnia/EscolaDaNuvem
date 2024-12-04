# Escreva um programa que leia um arquivo
# de texto contendo uma lista de números inteiros.Cada
# linha do arquivo contém um número.O programa deve calcular e exibir
# a soma ,a média, o maior e o menor valor do arquivo.

with open('numeros.txt', 'r') as arquivo:
    numeros = arquivo.readlines()
    numeros = [int(numero.strip()) for numero in numeros]
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    print(f'Soma: {soma}')
    print(f'Média: {media}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    