n, k = input().split()
n,k = int(n), int(k)

air = {}
for i in range(n):
    air[input()] = 1

line = {}
for i in range(1, k+1):
    line[i] = 0

q = int(input())

def free_line():
    for i in range(1, k+1):
        if not line[i]:
            return i
    return False

def TAKE_OFF(status):
    if status == 4:
        print('YOU ARE NOT HERE')
    elif status == 3:
        print('YOU ARE LANDING NOW')
    elif status == 2:
        print('YOU ARE TAKING OFF')
    elif (status == 1) and not (free_line()):
        print('NO FREE BOUND')
    else:
        line[free_line()] = st[1]
        status = 2
    return status
        

def LANDING(status):
    if status == 1:
        print('YOU ARE HERE')
    elif status == 2:
        print('YOU ARE TAKING OFF')
    elif status == 3:
        print('YOU ARE LANDING NOW')
    elif (status == 4) and not (free_line()):
        print('NO FREE BOUND')
    else:
        for i in range(k):
            if not line[k-i]:
                line[k-i] = st[1]
        status = 3
    return status

def PLANE_STATUS(status):
    print(status)
    return status

def BAND_STATUS(status):
    if line[status]:
        print(line[status])
    else:
        print('FREE')
    return status

fun = {'TAKE-OFF':TAKE_OFF,
       'LANDING':LANDING,
       'PLANE-STATUS':PLANE_STATUS,
       'BAND-STATUS':BAND_STATUS}

for i in range(q):
    st = input().split()
    try:
        air[st[1]] = fun[st[0]](air[st[1]])
    except:
        air[st[1]] = fun[st[0]](4)
