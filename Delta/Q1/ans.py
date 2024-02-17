n = int(input())
for row in range(n):
    line = ['.'] * (2 * n - 1)
    start = n - 1 - row
    end = n - 1 + row
    if row == n-1:
        for i in range(start, end + 1):
            if i % 2 == 0:
                line[i] = 'D'
            else:
                line[i] = '.'
    else:
        for i in range(start, end + 1):
            if (i == start) or (i == end):
                line[i] = 'D'
            else:
                line[i] = '.'
    print(''.join(line))


