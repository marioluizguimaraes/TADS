z1, z2, z3, z4 = map(int, input().split())

z1z2 = z1*z2
z1z3 = z1*z3
z1z4 = z1*z4
z2z3 = z2*z3
z2z4 = z2*z4
z3z4 = z3*z4

if (z1z2 == z3z4 or z1z3 == z2z4 or z1z4 == z2z3 ):
    print("S")
else:
    print("N")
