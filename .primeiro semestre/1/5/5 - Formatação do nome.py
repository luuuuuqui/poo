def formatar_nome(nome):
    partes = nome.split()
    partes = [parte.capitalize() for parte in partes]
    return ' '.join(partes)

a = input("Digite seu nome completo: ")
print(formatar_nome(a))