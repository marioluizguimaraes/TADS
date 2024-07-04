n = int(input())
conta = 0
if ( n <= 10):
    conta = 7
elif ( n >= 11 and n <= 30):
    conta = 7 + (n - 10)
elif ( n >= 31 and n <= 100):
    conta =  7 + 20 + (n - 30)*2
elif ( n >= 101): 
    conta =  7 + 20 + 140 + (n -100)*5

print(conta)
