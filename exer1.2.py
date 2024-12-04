# leia 2 valores inteiros e armazene-os nas variáveis A e B.
# Efetue a soma de a e b atribuindo o seu resultado na variável X.
# Imprima X conforma exemplo apresentado abaixo.
# Não apresente mensagem alguma além daquilo que está sendo especificado
# e não esqueça de imprimir o fim da linha
# após o resultado, caso contrário, você receberá "Presentation Error".
if __name__ == '__main__':
    a = int(input("Digite um número inteiro: " ))
    b = int(input("Digite outro número inteiro: "))
    x = a + b
    print("X = {}".format(x))