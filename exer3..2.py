# Com base na tabela abaixo escreva um programa
# que leia o código de um item e a quantidade deste item.
# A seguir, calcule e mostre o valor da conta a pagar.
# 1 cachorro quente R$4.00
# 2 x-salada R$4.50
# 3 x-bacon R$5.00
# 4 torrada simples R$2.00
# 5 refrigerante R$1.50
# Entrada
# O arquivo de entrada contém dois valores inteiros
# correspondentes ao código e à quantidade de um item
# conforme tabela acima.
# Saída
# O arquivo de saída deve conter a mensagem "Total: R$"
# seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
def calcular_valor(codigo, quantidade):
    if codigo == 1:
        return 4.00 * quantidade
    elif codigo == 2:
        return 4.50 * quantidade
    elif codigo == 3:
        return 5.00 * quantidade
    elif codigo == 4:
        return 2.00 * quantidade
    elif codigo == 5:
        return 1.50 * quantidade
    else:
        return 0.0
entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])
if codigo == 1:
    total = quantidade * 4.00
elif codigo == 2:
    total = quantidade * 4.50
elif codigo == 3:
    total = quantidade * 5.00
elif codigo == 4:
    total = quantidade * 2.00
elif codigo == 5:
    total = quantidade * 1.50



 # Define os preços dos itens
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# Função para calcular o total a pagar
def calcular_total(codigo, quantidade):
    if codigo in precos:
        total = precos[codigo] * quantidade
        return f"Total: R$ {total:.2f}"
    else:
        return "Código inválido"

# Leitura dos valores de entrada
codigo = int(input("Digite o código do item: "))
quantidade = int(input("Digite a quantidade: "))

# Cálculo e exibição do total
print(calcular_total(codigo, quantidade))