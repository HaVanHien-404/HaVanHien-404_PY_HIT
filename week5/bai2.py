print("nhap toa do hinh vuong thu nhat:")
a = list(map(int, input().split()))
print("nhap toa do hinh vuong thu 2:")
b = list(map(int, input().split()))
maxAx=a[0]
if a[0]<a[2]:
    maxAx=a[2]
maxAy=a[1]
if a[1]<a[3]:
    maxAy=a[3]
minBx=b[0]
if b[0]>b[2]:
    minBx=b[2]
minBy=b[1]
if b[1]>b[3]:
    minBy=b[3]
if (maxAx-minBx)<0:
    print("co bi trung dien tich khong bi trung la:")
    s=(maxAx-minBx)*(maxAy-minBy)
    print(s)
if(maxAx-minBx)>=0:
    print("khong trung va dien tich bawng tong 2 hinh:")
    print((a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1]))

