jogadores = [{'nome': 'Nelson', 'gols': [0, 2, 1], 'total': 3}, {'nome': 'Mario', 'gols': [2, 1, 3], 'total': 3}]
tot = 0

print('-'*35)
print(f'{"Cod":<5}{"Nome":<10}{"Gols":12}{"Total":<5}')
print('-'*35)

for c, e in enumerate(jogadores):
    print(f'{c:<5}{e["nome"]:<10}{e["gols"]}{e["total"]:>8}')
print('-'*35)


'''
for c, e in enumerate(jogadores):
    #print(f'{c:<5}{e["nome"]:<10}{e["gols"]}')
    for v in e.values():
        #print(e)
        print(v[0])
'''
'''
for c, e in enumerate(jogadores):
    for v in e.values():
        print(f'v = {v}')
        if type(v) == str:
            print(v)
            nome = v
        if type(v) == list:
            print(len(v))
            for c in range(len(v)):
                tot += v[c]
            print(tot)
'''