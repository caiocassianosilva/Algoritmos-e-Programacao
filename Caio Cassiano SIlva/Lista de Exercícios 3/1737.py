# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

quantNum = int(input())

somaNum = 0

if quantNum <= 0:
    print("Informe uma quantidade > 0!")
else:
    while quantNum > 0:
        numInf = float(input())
        somaNum = somaNum + numInf
        quantNum = quantNum - 1

    print("Soma dos números informados: %.2f" %(somaNum))
