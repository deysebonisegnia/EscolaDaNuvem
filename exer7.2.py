# Escreva um programa que leia um arquivo de 
# de texto e conte o número total de palavras,a
# palavras a quantidade distintas e o número de ocorrências de uma palavra
# específica (escolhida pelo usuário). O programa deve exibir essas informações.

with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    palavras = texto.split()
    total_palavras = len(palavras)
    palavras_distintas = set(palavras)
    quantidade_distintas = len(palavras_distintas)
    palavra_escolhida = input('Digite uma palavra: ')
    quantidade_palavra_escolhida = palavras.count(palavra_escolhida)
    print(f'Total de palavras: {total_palavras}')
    print(f'Quantidade de palavras distintas: {quantidade_distintas}')
    print(f'Quantidade de ocorrências da palavra "{palavra_escolhida}": {quantidade_palavra_escolhida}')