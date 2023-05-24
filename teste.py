# def veri_ana(palavra1, palavra2):
#     p1 = ''.join(sorted(palavra1.upper()))
#     p2 = ''.join(sorted(palavra2.upper()))
#     return print(p1 == p2)

# veri_ana('olha', 'aHol')

# def encontrar_sub_string(string, substring):
#     return print(substring in string)

# encontrar_sub_string('substring', 'string')
# encontrar_sub_string('valor', 'or')

# def quadrado(base, altura):
#     contador = 0
#     while contador < altura:
#         print('*  '*base)
#         contador += 1

# quadrado(3, 3)

def bordas(base, altura):
    linha = 0
    while linha < altura:
        if linha > 0 and linha < altura - 1:
            print('*  ','   '*(base - 3),' *')
        elif linha == altura:
            print('*  '*base)
        else:
            print('*  '*base)
        linha += 1

bordas(5, 7)