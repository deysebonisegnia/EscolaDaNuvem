# Escreva um programa para ler as coordenadas
# (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
# Para cada ponto escrever o quadrante a que ele pertence.
# O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA
# (nesta situação sem escrever mensagem alguma).

while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
     break
    elif x > 0 and y > 0:
        print("primeiro")
    elif x < 2 and y > 2:
        print("segundo")
    elif x < 3 and y < 3:
        print("terceiro")
    elif x > 4 and y < 4:
        print("quarto")
