a = int(input())
b = int(input())
c = int(input())

totalTime1 = (b * 2) + (c * 4)
totalTime2 = (a * 2) + (c * 2)
totalTime3 = (a * 4) + (b * 2)
print(min(totalTime1, totalTime2, totalTime3))