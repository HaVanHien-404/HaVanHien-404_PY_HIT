import math
i=1
n=int(input("nhap n:"))
for i in range(1,n+1):
    x=math.sqrt(i)
    if(x==int(x)):
        print(i)
