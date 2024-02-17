n, m = list(map(int, input().split(' ')))
r = []
for i in range(m):
    r.append(tuple(map(int, input().split(' '))))

computers = [0] * n

for s, l in r:
    for start_pos in range(s - 1, n - l + 1):
        if all(computer == 0 for computer in computers[start_pos:start_pos + l]):
            for i in range(start_pos, start_pos + l):
                computers[i] = 1
            break

    print(''.join(map(str, computers)))

