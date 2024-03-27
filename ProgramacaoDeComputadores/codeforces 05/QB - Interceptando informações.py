n7, n6, n5, n4, n3, n2, n1, n0 =  map(int, input().split())

if (( n0 == 0 or n0 == 1) and ( n1 == 0 or n1 == 1)):

    if ( ( n2 == 0 or n2 == 1) and ( n3 == 0 or n3 == 1)):

        if (( n4 == 0 or n4 == 1) and ( n5 == 0 or n5 == 1)):

            if (( n6 == 0 or n6 == 1) and ( n7 == 0 or n7 == 1)):

                print("S")
                
            else:
                print("F")
        else:
            print("F")
    else:
        print("F")
else:
    print("F")