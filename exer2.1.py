# Leia quatro valores inteiros A,B,C,D.A seguir ,
# calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: 
# DIFERENCA = (A * B - C * D).

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))
d = int(input("Digite outro número: "))

diferenca = (a * b - c * d)

print(f"DIFERENCA = {diferenca}")

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))
d = int(input("Digite outro número: "))

diferenca = (a * b - c * d)

print(f"DIFERENCA = {diferenca}")

while True:
    try:
        user_input = input("Digite um número: ").strip()
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        a = int(user_input)
        if a < -2**31 or a > 2**31 - 1:
            print("Number is too large. Please enter a number within the valid range.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    