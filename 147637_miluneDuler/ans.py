from numpy import ceil
T = input()
for i in range(int(T)):
    n, m, a, b = input().split()
    n, m, a, b = int(n), int(m), int(a), int(b)
    ans = (ceil((n-a+1) / ((2*a)-1))) * (ceil((m-b+1) / ((2*b)-1)))
    print(int(ans))