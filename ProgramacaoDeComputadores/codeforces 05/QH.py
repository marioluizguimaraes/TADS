A = int(input())
B = int(input())
C = int(input())
D = int(input())

AB_DC = (A + B) - (C + D)
AC_BD = (A + C) - (B + D)
AD_BC = (A + D) - (C + B)
if ( A + B == C + D or A + C == B + D or A + D == B + C):
    print("0")

elif ( AB_DC >= AC_BD and AB_DC >= AD_BC ):
    if(AB_DC < 0):
        print((AB_DC)*-1)
    else:
        print(AB_DC)

elif ( AC_BD >= AB_DC and AC_BD >= AD_BC ):
    if(AC_BD < 0):
        print((AC_BD)*-1)
    else:
        print(AC_BD)

elif ( AD_BC >= AB_DC and AD_BC >= AC_BD ):
    if(AD_BC < 0):
        print((AD_BC)*-1)
    else:
        print(AD_BC)