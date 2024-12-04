# faça um algoritmo para ler um número indeterminado
# de dados, contendo cada um, a idade de um indivíduo.
# O último dado, que não entrará nos cálculos, contém
# o valor de idade negativa. Calcular e imprimir a idade
# média deste grupo de indivíduos.

# Inicializa a variável 'soma' com 0 para armazenar a soma das idades
soma = 0

# Inicializa a variável 'cont' com 0 para contar o número de idades inseridas
cont = 0

# Loop infinito para ler as idades
while True:
    # Solicita ao usuário que insira a idade
    idade = int(input('Digite a idade: '))
    # Calcula a média das idades
    media = soma / cont
    soma += idade
    cont += 1 
    # Verifica se a idade é negativa
    if idade < 0:
        # Se for negativa, sai do loop
        break
    elif idade > 50:
        print(f'A média das idades é: {media}' )
        break
    # Se a idade for positiva, adiciona à soma e incrementa o contador
   

   # Imprime a média das idades
print(f'A média das idades é: {media}')