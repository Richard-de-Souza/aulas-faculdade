def eco(palavra: str):
    tamanho = len(palavra)
    eco = ''
    
    for letra in range(tamanho - 1, 0, -1):
        if palavra[letra:] == palavra[letra- (tamanho - letra):letra]:
            eco = palavra[letra:]
            break

    nova_palavra = palavra.replace(eco, (''))

    if eco:
        return [nova_palavra + eco] + [eco] * ((tamanho // len(eco) - 2))
    else:
        return [palavra]

resultado = eco("Olá")
print(resultado)

resultado = eco("Banana")
print(resultado)

resultado = eco("dudadadada")
print(resultado)

resultado = eco("Goooooooooooooo")
print(resultado)
