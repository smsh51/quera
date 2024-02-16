r1 = list(map(int, input().split(' ')))
r2 = list(map(int, input().split(' ')))
count = 0
for i in range(8):
    if r1[i] and r2[i]:
        count += 1
print(count)
