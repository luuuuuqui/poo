total = 0
rabbits = 0
rats = 0
frogs = 0

n = int(input())

for _ in range(n):
    allInputs = input().split()
    amount = int(allInputs[0])
    type = allInputs[1].upper()

    total += amount

    if type == 'C':
        rabbits += amount
    elif type == 'R':
        rats += amount
    elif type == 'S':
        frogs += amount

percentRabbits = (rabbits / total) * 100
percentRats = (rats / total) * 100
percentFrogs = (frogs / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {rabbits}")
print(f"Total de ratos: {rats}")
print(f"Total de sapos: {frogs}")
print(f"Percentual de coelhos: {percentRabbits:.2f} %")
print(f"Percentual de ratos: {percentRats:.2f} %")
print(f"Percentual de sapos: {percentFrogs:.2f} %")
