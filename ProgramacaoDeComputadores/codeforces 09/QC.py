clicks = int(input())
ordenClicks = list(map(int, input().split()))
a = 0
b = 0
for i in range(clicks):
    if (ordenClicks[i] == 1):
        if (a == 0):
            a = 1
        else:
            a = 0
    else:
        if (a == 0 and b == 0):
            a = 1
            b = 1
        elif (a == 1 and b == 0):
            a = 0
            b = 1
        elif (a == 0 and b == 1):
            a = 1
            b = 0
        else:
            a = 0
            b = 0
print(a)
print(b)