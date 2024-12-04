# ler um valor N .calcular e escrever seu
# rescpectivo fatorial .
# Fatorial de N = N (n-1) *(n-2)*(n-3)* ... *1

def calcular_fatorial(n):
    """ Função para calculo de fatorial de numero inteiro"""
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial
def main():
    try:
        N = int(input("Digite um numero inteiro entre 1 e 20: "))
        if N < 1 or N > 20:
            raise ValueError("O numero deve estar entre 1 e 20.")
        resultado = calcular_fatorial(N)
        print(f"O fatorial de {N} é: {resultado}")
    except ValueError:
        print("Valor invalido. Por favor, insira um numero inteiro entre 1 e 20.")
        if isinstance(N, int):
            print("O numero deve ser inteiro e entre 1 e 20")
main()