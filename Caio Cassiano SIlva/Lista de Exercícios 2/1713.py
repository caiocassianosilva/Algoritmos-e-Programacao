# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valHora = float(input())
numHora = float(input())

SB = valHora * numHora

IR = SB * (0.11)

INSS = SB * (0.08)

SIND = SB * (0.05)

SL = SB - (IR + INSS + SIND)

print("Salário bruto: R$%.2f" %(SB))
print("Imposto: R$%.2f" %(IR))
print("INSS: R$%.2f" %(INSS))
print("Sindicato: R$%.2f" %(SIND))
print("Líquido: R$%.2f" %(SL))
