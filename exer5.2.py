"""A seguinte sequencia de números 0,1,1,2,3,5,8,13,21 ... é 
 conhecida como série de Fibonacci. Nessa sequencia, cada número,
 depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um
 algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros
 números dessa série. Utilize o laço que lhe for mais conveniente."""
N = int(input())
a, b = 0, 1
for i in range(N):
    print(a)
    a, b = b, a + b         
    
    