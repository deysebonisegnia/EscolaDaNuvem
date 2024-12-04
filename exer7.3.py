# você foi contratado para trabalhar como Dev/AI Engineer na aws e 
# e esta responsável por monitorar o desempenho de modelos de Machine Learning
# Durante o treinamentos dos modelos,logs com dados de tempo de execução,
# precisão e perda do modelo são gerados.Esses logs estão armazenamento de uma arquivos de texto
# e cada linha do arquivo contém os dados do treinamento de um lote no  formato:BatchID,Tempo(seg),Precisao(%),
# Perda.Sua tarefa é processar esse arquivo de logs,calcular as seguintes estatísticas e exibir os resultados:
# o tempo total de treinamento 
# A precisão média, O lote com a maior  precisão e o lote com menor precisão.
# O número de lotes com perda superior a 0.5 e o número de lotes com perda superior a 1.0.
# O programa deve exibir essas informações.

with open('logs.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    tempo_total = 0
    precisao_total = 0
    lote_maior_precisao = 0
    lote_menor_precisao = 100
    lotes_perda_maior_50 = 0
    lotes_perda_maior_100 = 0
    for linha in linhas:
        dados = linha.split(',')
        batch_id = dados[0]
        tempo = float(dados[1])
        precisao = float(dados[2])
        perda = float(dados[3])
        tempo_total += tempo
        precisao_total += precisao
        if precisao > lote_maior_precisao:
            lote_maior_precisao = precisao
            lote_maior_precisao_batch_id = batch_id
        if precisao < lote_menor_precisao:
            lote_menor_precisao = precisao
            lote_menor_precisao_batch_id = batch_id
        if perda > 0.5:
            lotes_perda_maior_50 += 1
        if perda > 1.0:
            lotes_perda_maior_100 += 1
    precisao_media = precisao_total / len(linhas)
    print(f'Tempo total de treinamento: {tempo_total} segundos')
    print(f'Precisão média: {precisao_media:.2f}%')
    print(f'Lote com maior precisão: {lote_maior_precisao_batch_id} com {lote_maior_precisao:.2f}%')
    print(f'Lote com menor precisão: {lote_menor_precisao_batch_id} com {lote_menor_precisao:.2f}%')
    print(f'Número de lotes com perda superior a 0.5: {lotes_perda_maior_50}')
    print(f'Número de lotes com perda superior a 1.0: {lotes_perda_maior_100}')

