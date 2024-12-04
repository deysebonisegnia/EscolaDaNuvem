# Leia 100 valores inteiros.
# Apresente então o maior valor lido 
# e a posição dentre os 100 valores lidos.

maior = 0
posicao = 0

for i in range(100):
    valor = int(input())
    if valor > maior:
        maior = valor
        posicao = i + 1

print(maior)
print(posicao)