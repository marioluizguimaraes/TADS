z1, z2, z3, z4 = map(int, input().split())

if (z1 >= z2 and z1 >= z3 and z1 >= z4):
    if(z1 >= z2 + z3 + z4):
        print("S")
    else:
        print("N")
elif (z2 >= z1 and z2 >= z3 and z2 >= z4):
    if (z2 >= z1 + z3 + z4):
        print("S")
    else:
        print("N")

elif (z3 >= z1 and z3 >= z2 and z3 >= z4):
    if (z3 >= z1 + z2 + z4):
        print("S")
    else:
        print("N")

elif (z4 >= z1 and z4 >= z2 and z4 >= z3):
    if (z4 >= z1 + z2 + z3):
        print("S")
    else:
        print("N")