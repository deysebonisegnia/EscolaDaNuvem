# Leia quatro números (N1,N2,N3,N4),cada um deles
# com uma casa decimal,correspondetendo as notas dos
# alunos. Em seguida, calcule a média com pesos 2, 3, 4 e 1,
# respectivamente, para cada uma destas notas e mostre
# esta média acompanhada pela mensagem "Media: ". Se esta
# média for maior ou igual a 7.0, imprima a mensagem
# "Aluno aprovado.". Se a média calculada for inferior a 5.0,
# imprima a mensagem "Aluno reprovado.". Se a média calculada
# for um valor entre 5.0 e 6.9, inclusive estas, o programa deve
# imprimir a mensagem "Aluno em exame.".
# No caso do aluno estar em exame, leia uma quarta nota
# correspondente à nota do exame. Refaça o cálculo da média
# da primeira e da segunda prova. Se esta média for maior ou
# igual a 5.0, imprima a mensagem "Aluno aprovado.".
# Caso contrário, imprima a mensagem "Aluno reprovado.".
# Imprima também a mensagem "Media final: " seguida da média
# final para esse aluno.

n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: %.1f" % media)
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: %.1f" % nota_exame)
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % media_final)