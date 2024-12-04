# Faça um programa que leia as notas referentes ás 
# duas avaliações de um aluno.Calcule e imprima a média semestral.
# Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]).
# Cada nota deve ser validada separadamente.
nota1 = float(input('Informe a primeira nota: '))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input('Nota inválida. Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input('Nota inválida. Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média do aluno é {media}') 