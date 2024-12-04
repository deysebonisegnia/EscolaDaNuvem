# Deve-se ler o código de uma peça 1,o número de 
# peças 1, o valor unitário de cada peça 1. O código de uma peça 2,
# o número de peças 2 e o valor unitário de cada peça 2. 
# Após, calcule e mostre o valor a ser pago.

codigo1,num1,valor1 = (input()).split()
codigo1 = int(codigo1)
num1 = int(num1)
valor1 = float(valor1)
codigo2, num2, valor2 = input().split()
codigo2 = int(codigo2)
num2 = int(num2)
valor2 = float(valor2)

total = (num1 * valor1) + (num2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")