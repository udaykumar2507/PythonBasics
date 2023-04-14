#BASIC LIST PROBLEM
#PROGRAM TO FIND SUM OF ELEMENTS IN THE LIST
print("sum of elements")
A=[]
n=int(input("enter the element"))
sum=0
for i in range(n):
    x=int(input("enter the element:"))
    A.append(x)
    sum+=x
print(A)
print("the sum  of the total num is",sum)
#PROGRAM TO COUNT TOTAL NUMBER OF OD AND EVEN PROGRAM IN A LIST
print("total odd and even")
A=[]
n=int(input("enter the number"))
odd=0
even=0
for i in range(n):
    x=int(input("enter the value:"))
    if x%2==0:
        even+=1
    else:
        odd+=1
    A.append(x)
print("the even is",even)
print("the num of oddd is",odd)
print(A)
#PROGRAM TO SEARCH A NUMBER IN A LIST
print("search a num in a list")
A=[]
n=int(input("enter the number:"))
for i in range(n):
    x=int(input("enter the element:"))
    A.append(x)
search=int(input("enter the num to serach"))
for i in range(n):
    if A[i]==search:
        print("element found at ",i+1)
        break
else:
    print("element not found")       
#PRINT TO COUNT THE FREQUENMCY OF THE GIVEN N UMBER
print("frequency of count")
A=[]
count=0
n=int(input("enterthe number"))
for i in range(n):
    x=int(input("enter the value"))
    A.append(x)
print(A)
num=int(input("enter the num"))
for i in range(n):
    if A[i]==num:
        count+=1
print("the num of count is",count)
#find max in a list
print("find max")
a=[]
n=int(input("enter:"))
for i in range(n):
    x=int(input("enter     :"))
    a.append(x)
print(a)
max=a[0]
for i in range(1,n):
    if max<a[i]:
        max=a[i]
print("max is",max)
#find min in a list
print("find min")
a=[]
for i in range(5):
    n=int(input("enter:"))
    a.append(n)
for  i in range(n):
    min=a[0]
    if a[i]<min:
        min=a[i]
print("the min is",min)
#program to print a reverse a list
print("reverse a list")
a=[]
n=int(input("enter the num:"))
for i in range(n):
    n1=int((input("enter the num")))
    a.append(n1)
print("the revrese is")
for i in range(n-1,-1,-1):
    print(a[i],end="")
#program to find first and second min
a=[]
n=int(input("enter the num"))
for i in range(n):
    x=int(input("enter the value"))
    a.append(x)
print(a)
print(a.sort())
print("the first min is",a[0])
print("the second min is",a[1])
#anothr one
a=[]
n=int(input("enter the num"))
for i in range(n):
    n1=int(input("enter the num"))
    a.append(n1)
print(a)
c=min(a)
print("the min is",c)
a.remove(c)
print("the second min",min(a))