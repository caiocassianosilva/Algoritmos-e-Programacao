# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input()
numHorasEx = float(input())

valHoraEx = 10.00
salMin = 1192.40
salHoraEx = numHorasEx * valHoraEx
salBruto = 3 * salMin + salHoraEx

if salBruto > 2000.00:
    INSS = salBruto * 0.12
else:
    INSS = salBruto * 0.05

if salBruto > 2500.00:
    IR = salBruto * 0.2
else:
    IR = 0

salLiq = salBruto - (INSS + IR)

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" %(salLiq))
