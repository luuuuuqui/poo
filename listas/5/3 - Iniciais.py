def iniciais(nome):
    partes = nome.split()
    iniciais = [parte[0].upper() for parte in partes]
    return '.'.join(iniciais) + '.'

a = input("Digite seu nome completo: ")
print(iniciais(a))