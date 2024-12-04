# A formula para calcular a área de uma circunferência é :área = pi * raio ** 2. 
# Considerando para este problema que pi = 3.14159: - Efetue o cálculo da área, 
# elevando o valor de raio ao quadrado e multiplicando por pi.
# apresente a mensagem "A = " seguindo pelo valor da variável area,
# conforme o exemplo abaixo ,com 4 casas após o ponto decimal.
# Utilize variável de dupla precisão (double).

def areaDoCirculo():
    Raio = float(input("Digite a área do círculo: "))
    Pi = 3.14159
    Area = Pi * (Raio ** 2)

    print("A = %0.4f"%Area)
    print("Area = ",Area)
areaDoCirculo()
   