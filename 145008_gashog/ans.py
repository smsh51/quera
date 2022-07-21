n = int(input())
g = input()
i = 0
while i < n:
    if g[i] == g[i+n]:
        print('NO')
        break
    i+=1
else:
    print('YES')
