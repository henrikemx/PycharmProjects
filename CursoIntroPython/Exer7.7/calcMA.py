###########################################
# Após assistir e recapitular conceitos de 
# variável do tipo LISTA da aula 17 do Curso
# em Python do canal Curso em Video irei, à
# seguir aplicar esses conhecimentos ao exer-
# cício proposto na apostila para cálculo de
# Média Aritmética, Média Geométrica e Média
# Harmônica...
############################################

# declaração da variável
media = []
soma = 0

# informar os avlores das notas bimestrais...
for c in range(0, 5):
    media.append(float(input(f'Informe a {c}ª nota: ')))

# expressão para cálculo da M.A.
# ma = (n1 + n2 + n3 + n4) / 4
# tentando calcular usando loop for
for n in range(0, len(media)):
    soma += media[n]
ma = soma / 4

# apresentação do resultado...
print(f'O valor da M.A. do aluno foi de \033[33m{}\033[0;0m.')
