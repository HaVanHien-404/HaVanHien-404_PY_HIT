n=input("nhap so cau h:")
a=[]
for i in n:
    a.append(input("nhap ten ban trả lời đúng:"))
dem=0
for k in range(0,n,1):
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if (a[i] == a[j]):
                dem+=1
    y.append(dem)
    break


for i in range(0,n,1):
    if max(y)==y[i]:
        print(a[i])
####    em chưa biết làm bài này

