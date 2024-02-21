n, V = list(map(int, input().split(' ')))
h, v = list(range(n)), list(range(n))
for i in range(n):
    h[i], v[i] = list(map(int, input().split(' ')))

s = 0
for j in range(n):
    i = h.index(max(h))
    if v[i]/V <= 1:
        V -= v.pop(i)
        s += h.pop(i)
    else:
        s += h[i] / (v[i]/V)
        break

print(round(s, 1))