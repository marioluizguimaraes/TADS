Ca, Ba, Pa = map(int, input().split())
 
Cr, Br, Pr = map(int, input().split())
 
Nc = Ca - Cr
Nb = Ba - Br
Np = Pa - Pr
 
if ( Nc < 0 and Nb < 0 and Np < 0):
    print(-1*(Nc+Nb+Np))
 
elif ( Nc < 0 and Nb < 0 ):
    print(-1*(Nc+Nb))
 
elif ( Nc < 0 and Np < 0 ):
    print(-1*(Nc+Np))
 
elif ( Nb < 0 and Np < 0 ):
    print(-1*(Nb+Np))
 
elif ( Nb < 0 ):
    print(-1*Nb)
 
elif ( Nc < 0 ):
    print(-1*Nc)
 
elif ( Np < 0 ):
    print(-1*Np)
 
else:
    print("0")