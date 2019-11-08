n=int(input("nhap n:"))
a=[]
for i in range(n):
    a.append(int(input('Nhap so thu %d: ' % (i+1))))

b=[]
for i in range(n):
    b.append(int(input('Nhap so thu %d: ' % (i+1))))
print(a)
print(b)
b.reverse()

x=[]

x=a+b

y=[]
for i in range(0,n,1):
    for j in range(0,n,1 ):
        y.append(x[j] + x[- j-1])

    break
print(y)