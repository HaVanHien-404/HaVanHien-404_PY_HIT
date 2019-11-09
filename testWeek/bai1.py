n=int(input("nhập số lượng gói kẹo:"))
a=[]
for i in range(0,n,1):
    a.append(int(input("nhập số lượng kẹo trong gói thứ %d" %(i+1))))
tong=0
for i in range(n):
    tong+=a[i]
m=a[0]
for i in range(n):
    if m==(tong-1) or m==(tong-2)or m==(tong-3) or m==(tong+1) or m==(tong+2) or m==(tong+3) or m==tong:
        print(i)
    else:
        m=m+a[i]
