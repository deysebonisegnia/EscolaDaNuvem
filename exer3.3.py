# Leia o salário do funcionário e calcule e mostre
# o novo salário, bem como o valor de reajuste
# ganho e o índice reajustado, em percentual.

# Função para calcular o novo salário, valor de reajuste e índice reajustado
def calcular_reajuste(salario):
    if salario <= 400.00:
        percentual = 15
    elif salario <= 800.00:
        percentual = 12
    elif salario <= 1200.00:
        percentual = 10
    elif salario <= 2000.00:
        percentual = 7
    else:
        percentual = 4

    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste

    return novo_salario, reajuste, percentual

# Leitura do salário do funcionário
salario_atual = float(input("Digite o salário do funcionário: "))

# Cálculo do novo salário, valor de reajuste e índice reajustado
novo_salario, reajuste, percentual = calcular_reajuste(salario_atual)

# Exibição dos resultados
print(f"Novo salário: R$ {novo_salario:.2f}")
print(f"Reajuste ganho: R$ {reajuste:.2f}")
print(f"Em percentual: {percentual} %") 
