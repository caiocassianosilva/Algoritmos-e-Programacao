# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

N = int(input())

contador = 1
resultado = 1
while contador <= N:
    resultado = contador * resultado
    contador = contador + 1

print("%i! = %i" %(N, resultado))
