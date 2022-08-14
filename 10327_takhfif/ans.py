n, t = input().split()
n, t = int(n), set(t)
for i in range(n):
    x = set(input())
    if x == t:
        print('Yes')
    else:
        print('No')