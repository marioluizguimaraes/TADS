n    = int(input())
c100 = n//100
c50  = (n - (100*c100))//50
c20  = (n - ((100*c100) + c50*50))//20
c10  = (n - (((100*c100) + c50*50) + c20*20))//10
c5   = (n - ((((100*c100) + c50*50) + c20*20) + c10*10))//5
c2   = (n - (((((100*c100) + c50*50) + c20*20) + c10*10) + c5*5))//2
c1   = (n - ((((((100*c100) + c50*50) + c20*20) + c10*10) + c5*5) + c2*2))//1

print(n)
print(c100, "nota(s) de R$ 100,00")
print(c50, "nota(s) de R$ 50,00")
print(c20, "nota(s) de R$ 20,00")
print(c10, "nota(s) de R$ 10,00")
print(c5, "nota(s) de R$ 5,00")
print(c2, "nota(s) de R$ 2,00")
print(c1, "nota(s) de R$ 1,00")
