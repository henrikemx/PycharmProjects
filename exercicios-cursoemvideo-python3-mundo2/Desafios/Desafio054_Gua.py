# Enunciado: desenvolva um programa que leia o ano de nascimento de 7 pessoas
#  e, no final, quantas delas ainda não atingiram a maioridade (21 anos) e,
# destas, quantas são maiores.

from datetime import date
ano = date.today().year
pessoas = 0

for c in range(1, 7 + 1):
    msg = 'Digite o ano de nascimento da pessoa Nº {}: '.format(c)
    data = int(input(msg))
    if ano - data >= 21:
        pessoas += 1

if pessoas == 0:
    print('Todas as 7 pessoas ainda são menores de idade.')
elif pessoas == 1:
    print('6 pessoas ainda são menores de idade. Somente 1 já atingiu a maioridade.')
else:
print('Das 7 pessoas, {} são menores de idade e {} já atingiram a maioridade.'.format(7 - pessoas, pessoas))