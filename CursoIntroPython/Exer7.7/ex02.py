#####################################################################
# Abelindo é um professor muito malvado. Ele quer decidir como reprovar
# Rondinelly, que tirou 8.66, 5.35, 5 e 1, respectivamente, nas provas
# P1, P2, P3 e P4. Para isso, ele pode calcular a nota final usando
# média aritmética (M.A.), média geométrica (M.G.) ou média harmônica (M.H.).
#
#   M.A. = (p1 + p2 + p3 + p4)/4
#
#   M.G. = 4V(P1 * P2 * P3 * P4)
#
#   M.H. = 4/(1/P1 + 1/P2 + 1/P3 + 1/P4)
#
# Qual dessas médias dá a maior nota pra Rondinelly? E qual das médias
# dá a pior nota?
#####################################################################

print('#'*40)
# declarando as variáveis...
p1 = 8.66
p2 = 5.35
p3 = 5
p4 = 1
maior = menor = 0

ma = (p1 + p2 + p3 + p4)/4
mg = (p1 * p2 * p3 * p4) ** (1/4)
mh = 4/(1/p1 + 1/p2 + 1/p3 + 1/p4)

print('Se as notas de Rondinelly foram, respectivamente,\n 8.66, 5.35, 5 e 1, então as médias encontradas foram...\n')
print(f'=> M.A. = {ma:.2f}\n')
print(f'=> M.G. = {mg:.2f}\n')
print(f'=> M.H. = {mh:.2f}\n')

print('#'*40)
print(f'Logo, a maior média foi de {ma:.2f} e a menor de {mh:.2f}')

for cnt in range(0, 4):
    if cnt = 0:

    if ma < mg > mh:
        maior = ma
        menor = ma
    if mg > ma or mg > mh:
        maior = mg
        menor = mg
    if mh > ma or mh > mg:
        maior = mh
        menor = mh

print(f'=> Logo, a MAIOR média foi {maior} e a MENOR foi {menor}')
