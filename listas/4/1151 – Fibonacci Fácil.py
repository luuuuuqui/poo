n = int(input())

a = 0
b = 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b