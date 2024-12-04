# Dadas as informações de população e a taxa de crescimento de duas cidades quaisquer (A e B), faça um programa que
# calcule e escreva o número de anos necessários para que a cidade menor (sempre é a cidade A) ultrapasse a cidade B,
# mantendo as taxas de crescimento.
cidade_a = int(input('Informe a população da cidade A: '))
cidade_b = int(input('Informe a população da cidade B: '))
taxa_a = float(input('Informe a taxa de crescimento da cidade A: '))
taxa_b = float(input('Informe a taxa de crescimento da cidade B: '))
anos = 0

while cidade_a < cidade_b:
    cidade_a = cidade_a + (cidade_a * taxa_a)
    cidade_b = cidade_b + (cidade_b * taxa_b)
    anos += 1
print(f'A cidade A ultrapassará a cidade B em {anos} anos.')

def calcular_anos (PA, PB, G1, G2):
    anos = 0
    while PA <= PB:
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1

        if anos > 100:
            return "Mais do que 1 século/100 anos"
    
    return anos

def main():
    try:
        T = int(input("Digite o numero de casos de teste: "))
        if T < 1 or T > 3000:
            raise ValueError("O número de casos de teste deve estar entre 1 e 3000.")
        for T in range(T):
            valores = input("Digite PA, PB, G1, G2: ").split()
            PA, PB = int(valores[0]), int(valores[1])
            G1, G2 = float(valores[2]), float(valores[3])

            resultado = calcular_anos(PA, PB, G1, G2)

        print(resultado)
    except ValueError as ve:
        print(f"Erro: {ve}")
    
main()