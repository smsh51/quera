# create by SmS.hZ
xt, yt = list(map(int, input().split()))
xb, yb = list(map(int, input().split()))
if (xt >= xb) and (yt >= yb):
    print('yes')
else:
    print('no')