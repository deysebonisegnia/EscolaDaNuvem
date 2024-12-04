#Escreva um programa que leia o número de um funcionário, 
# seu número de horas trabalhadas, o valor que recebe por hora e 
# calcula o salário desse funcionário. A seguir, mostre o número e 
# o salário do funcionário, com duas casas decimais.

num = int(input("Digite o número do funcionário: "))
horas = int(input("Digite o número de horas trabalhadas: "))
valor = float(input("Digite o valor das horas trabalhadas: "))

salario = horas * valor

print("NUMBER = %i" %num)
print("SALARY = U$ %.2f" %salario)

try:
    num = int (input("Digite o número do funcionário: "))
except ValueError:
    print("Valor inválido.Por favor, digite um número inteiro.")
finally:
    print("programa encerrado")