import math

a=float(input("nhap canh a:"))
b=float(input("nhap canhj b:"))
c=float(input("nhap canh c:"))
p=(a+b+c)/2
if((a+b>=c or b+c>=a or c+a>=b)and(a>0 and b>0 and c>0)):
    print("canh daif nhat la",max(a,b,c))
    print("dien tich tam giac=",(math.sqrt(p*(p-a)*(p-b)*(p-c))))
    print("chu vi tam giac =",(a+b+c))
else:
    print("khong phai tam giac")
