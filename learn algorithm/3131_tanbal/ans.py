# create by SmS.hZ
x, y = list(map(int, input().split()))

print(1)
for i in range(6):
    if ((7-i) != x) and ((7-i) != y):
        print(7-i, 7-i)
        break
