# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

PT = input("")
salAtual = float(input())

A = 0.10
B = 0.15
C = 0.20


novoSal1 = salAtual + (salAtual * A)
novoSal2 = salAtual + (salAtual * B)
novoSal3 = salAtual + (salAtual * C)

if PT == "A" :
    print("Novo salário: R$%.2f" %(novoSal1))
elif PT == "B" :
    print("Novo salário: R$%.2f" %(novoSal2))
elif PT == "C" :
    print("Novo salário: R$%.2f" %(novoSal3))
