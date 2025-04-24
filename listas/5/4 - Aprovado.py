def aprovado(nota1, nota2):
    return ((nota1 * 2 + nota2 * 3) / 5) >= 6

a = float(input("Digite a nota do primeiro bimestre da disciplina:\n"))
b = float(input("Digite a nota do segundo bimestre da disciplina:\n"))

print(f"Você está {'Aprovado' if aprovado(a, b) else 'Reprovado'}.")