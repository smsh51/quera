a, b = input().split()
a, b = int(a), int(b)
if a == 0 and b == 0:
    print('infinite')
else:
    try:
        -b/a
        print('unique')
    except:
        print('invalid')

