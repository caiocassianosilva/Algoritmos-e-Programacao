# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

qtdPessoa = 4
cont90 = 0
idade = 0

while qtdPessoa > 0:
    idade1 = int(input())
    peso = float(input())

    if peso > 90:
        cont90 = cont90 + 1
        idade = idade1 + idade
        qtdPessoa = qtdPessoa - 1

    else:
        idade = idade1 + idade
        qtdPessoa = qtdPessoa - 1

media = idade / 4
print("Qtd pessoas > 90 Kg: %i" %(cont90))
print("Idade média: %.2f" %(media))
