# você trabalha como Dev/AI Engineer na AWSe está responsavel por analisar os 
# custos de diferentes serviços em uma conta AWS.Os logs de uso dos serviço 
# são gerados em um arquivos de texto ,onde cada linha contém o nome do serviço 
# e o custo associado a ele. Escreva um script em Python que leia esse arquivo
# e calcule o custo total de todos os serviços.

def calcular_custo_total(arquivo):
    custo_total = 0
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            if len(partes) == 2:
                nome_servico, custo = partes
                custo = float(custo)
                custo_total += custo
    return custo_total

arquivo_logs = 'logs.txt'
custo_total = calcular_custo_total(arquivo_logs)
print(f'O custo total dos serviços é: R${custo_total:.2f}')

calcular_custo_total(arquivo_logs)
