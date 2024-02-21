n, V = list(map(int, input().split(' ')))
j = []
for i in range(n):
    h, v = list(map(int, input().split(' ')))
    j.append((h / v, v))

j.sort(reverse=True)

th, vc = 0, 0
for happiness, volume in j:
    if vc + volume <= V:
        # If the entire volume of this juice can be consumed
        th += happiness * volume
        vc += volume
    else:
        # If only a part of this juice can be consumed
        rv = V - vc
        th += happiness * rv
        break

print(round(th, 1))