a = []

for i in range(0, 100):
    a.append(int(input()))

print(max(a))
print(a.index(max(a)) + 1)