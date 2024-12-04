# você deve imprimir a mensagem "Hello World" 
if __name__ == '__main__':
    print("Hello World")
    
# Este programa exibe uma saudaçao  personalizada   
def saudacao(name):
    print("Ola, " + name + "! Seja bem vindo(a)") 
    
name_user = input("Digite seu nome: ")
saudacao(name_user)
