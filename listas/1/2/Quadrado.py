a = float(input("Digite a base e a altura do retângulo\n"))
b = float(input())

area = a * b
perimeter = 2 * (a + b)
diagonal = (a**2 + b**2) ** 0.5

print(f"Área = {area:.2f} - Perímetro = {perimeter:.2f} - Diagonal = {diagonal:.2f}")