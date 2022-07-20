n = input()
t = input().split()
def X(i):
    if int(i)>15:
        print('cooler')
    else:
        print('heater')
list(map(X, t))