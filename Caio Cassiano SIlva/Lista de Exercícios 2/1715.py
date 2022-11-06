# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

COMUM = 1
FUNCIONARIO = 2
PREMIUM = 3

TC = int(input())
VTC = float(input())

desFun = VTC - (VTC * 0.13)
desPre = VTC - (VTC * 0.07)

if TC == 1 :
    print("Valor total a ser pago: R$%.2f" %(VTC))
elif TC == 2 :
    print("Valor total a ser pago: R$%.2f" %(desFun))
elif TC == 3 :
    print("Valor total a ser pago: R$%.2f" %(desPre))
else :
    print("OPÇÃO INVÁLIDA!")
