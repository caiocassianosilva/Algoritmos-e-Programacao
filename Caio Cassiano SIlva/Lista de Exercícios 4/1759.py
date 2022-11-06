# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

atual = int(input())
valIni = 1015
valorSomado = 1015
contadorPorcentagem = 0.015
somaPorcentagem = 0.01

anos = atual - 2006

if atual < 2006:
    print("O ano informado deverá ser > 2005!")

elif atual == 2006:
    print("Salário atual: R$%.2f" %(valIni))

elif atual > 2006:
    porcentagem = (0.015 + 0.01)
    anterior = valIni

    for x in range(anos):
        calculo = anterior + (anterior * porcentagem)
        anterior = calculo
        porcentagem = porcentagem + 0.01

    print("Salário atual: R$%.2f" %(calculo))
