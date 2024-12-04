# faça um programa que leia o  nome de vendedor,o seu salário fixo 
# e o total de vendas efetuadas por ele no mês (em dinheiro).
# sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
# informar o total a receber no final do mês, com duas casas decimais.

nome = input("Digite o nome do vendedor: ")
salario = float(input("Digite o salário fixo do vendedor: "))
vendas = float(input("Digite o total de vendas efetuadas pelo vendedor no mês (em dinheiro): "))

comissao = vendas * 0.15
salario_final = salario + comissao

print(f"TOTAL = R$ {salario_final:.2f}")