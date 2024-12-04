#leia dois valores inteiros A e B.A seguir ,calcule
#a soma entre elas e atribua à variável SOMA.A seguir escrever o 
# valor desta variável.

A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))
SOMA = A + B
print("SOMA = ",SOMA)

def get_valid_number():
    while True:
        try:
            number_input = (input("Por favor,digite um número inteiro válido: "))
            number = int(number_input)
            return number
        except ValueError:
            print("Valor inválido.Por favor, digite um número inteiro.")
            
number = get_valid_number()
            
