#Tanque de combustível
c = int(input())
d = int(input())
l = int(input())

total = (d/c) - l

if (total <= 0):
    total = 0
    print("{:.1f}".format(total))
else:
    print("{:.1f}".format(total))
