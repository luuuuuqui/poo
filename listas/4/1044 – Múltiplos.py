import math

a, b = map(int, input().split())
mmc = math.gcd(a, b)
if mmc == min(a, b):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
