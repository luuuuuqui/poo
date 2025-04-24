def maior(x, y):
    if x > y:
        return x
    else:
        return y

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"O maior número é: {maior(a, b)}")