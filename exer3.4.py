# leia 4 valores inteiros A,B,C,D.A 
# seguir se Bfor maior do que C e se D for maior
# do que A e a soma de C com D for maior que a 
# soma de A e B e se C e D, ambos, forem positivos
# e se a variável A for par escrever a mensagem "Valores aceitos",
# senão escrever "Valores nao aceitos".

a, b, c, d = map(int, input().split())

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
    
    # Função para verificar os valores conforme as condições especificadas
def verificar_valores(A, B, C, D):
    if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
        return "Valores aceitos"
    else:
        return "Valores nao aceitos"

# Leitura dos valores inteiros A, B, C, D
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Verificação e exibição do resultado
resultado = verificar_valores(A, B, C, D)
print(resultado)
