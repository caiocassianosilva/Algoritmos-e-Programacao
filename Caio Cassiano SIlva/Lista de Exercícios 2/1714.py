# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

PC = float(input())
A = 20.00

BC = PC + (PC * 0.45)

MC = PC + (PC * 0.30)

if PC < A :
    print("Valor de venda: R$%.2f" %(BC))

else :
    print("Valor de venda: R$%.2f" %(MC))
