# faça um programa que apresente a sequencia
#conforme o exemplo abaixo I=1 J=7
#I=1 J=6
#I=1 J=5
#I=3 J=9
#I=3 J=8
#I=3 J=7
#I=5 J=11
#I=5 J=10
#I=5 J=9
#I=7 J=13
#I=7 J=12
#I=7 J=11
#I=9 J=15
#I=9 J=14
#I=9 J=13
I = 1
J = 7
while I <= 9:
    for i in range(3):
        print(f"I={I} J={J}")
        J -= 1
    I += 2
    J += 5