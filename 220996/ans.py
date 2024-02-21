t = int(input())
for j in range(t):
    n = int(input())
    x = float(input())
    SUM = 0
    for i in range(n):
        SUM += int(x + (i/n))
    print(SUM)
