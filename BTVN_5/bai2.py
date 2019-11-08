n=int(input("nhap n:"))
a=[]
for i in range(n):
    a.append(int(input('Nhap so thu %d: ' % (i+1))))
m=int(input("nhap m:"))
b=[]
for i in range(m):
    b.append(int(input('Nhap so thu %d: ' % (i+1))))
y=[]
for k in range(0,m+n,1):
    for i in range(0,n,1):
        for j in range(0,m,1):
            if a[i] == b[j]:
                y.append(a[i])

    break

y=set(y)

print(y)
