def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def expansion(n):
    t = []
    for k in range(n+1):
        c = coefficient(n, k)
        x = n - k
        y = k
        term = ''
        if c != 1:
            term += str(c)
        if x > 0:
            term += 'x'
            if x > 1:
                term += '^' + ('{' + str(x) + '}' if x > 9 else str(x))
        if y > 0:
            term += 'y'
            if y > 1:
                term += '^' + ('{' + str(y) + '}' if y > 9 else str(y))
        t.append(term)
    return '+'.join(t)


n = int(input())
print(expansion(n))
