import random

n = int(input("nhập vào số phần tử mảng:"))
a = []

for i in range(n):
    a.append(int(input("nhập phần tử thứ %d" % (i + 1))))
m = int(len(a) * 0.3)
k = len(a) - m
c = []
for j in range(m):
    for i in range(n):
        c.append(random.sample(a[i], m))
    break
print(c)
for i in range(n):
    for j in range(m):
        if a[i] == c[j] and a[i + 1] == c[j + 1] and a[i + 2] == c[j + 2]:
            del a[i:i + 3]

    break
print(a)
