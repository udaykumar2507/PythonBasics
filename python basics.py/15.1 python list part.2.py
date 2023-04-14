#TO PRINT THE MIN IN A LISY
a=[]
n=int(input("enetr the num:"))
for i in range(n):
    x=int(input("enmter the num:"))
    a.append(x)
print(a)
min=a[0]
for i in range(1,n):
    if a[i]<min:
        min=a[i]
print("min is",min)       
#PROGRAM TO REVERSE A LIST
A=[]
n=int(input('enter the num:'))
for i in range(n):
    x=int(input('enter the num'))
    A.append(x)
print(A)
for i in range(n-1,-1,-1):
    print(A[i],end=",")
#another one
print(A[-1::-1])