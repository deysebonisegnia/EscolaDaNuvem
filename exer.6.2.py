# A empresa ABC resolveu conceder um aumento de 
# de salários a seus funcionário de acordo com a tabela abaixo:
# Salário	Percentual de Reajuste
# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00
# 10%
# 7%
# 4%
# 23%
# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho.
# Exemplo de Entrada	Exemplo de Saída
# 400.00
# Novo salario: 460.00
# Reajuste ganho: 60.00
# Em percentual: 15 %
# 800.01
# Novo salario: 880.01
# Reajuste ganho: 80.00
# Em percentual: 10 %
# 2000.00
# Novo salario: 2140.00
# Reajuste ganho: 140.00
# Em percentual: 7 %

salario = float(input())
if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4
reajuste = salario * percentual / 100
novo_salario = salario + reajuste
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")