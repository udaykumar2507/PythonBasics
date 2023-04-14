'''TYPES OF OPERATORS'''
#ARITHMATIC OPERATORS
a=10
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
#relational operator
a1=5
b1=7
print(a1<b1)
print(a1>b1)
print(a1==b1)
print(a1<=b1)
print(a1>=b1)
print(a1!=b1)
#assigment operators
a2=15
b2=6
c=0
c+=b2
print(c)
c-=b2
print(c)
c*=a2
print(c)
c/=a2
print(c)
c%=a2
print(c)
#logical operator
#we have to find the max between three numbers
a=int(input("enter the first num:"))
b=int(input("enter the second numbers:"))
c=int(input("enter the third number"))
if (a>b) and (a>c):
    print(a,"is max")
elif (b>c) and (b>a):
    print(b,"is max")
else:
    print(c,"is max")    
#example2     
#time to check working hours
time=int(input("enter the time"))
time1="sunday"
if (time>18) or(time<9): 
    print("not working hours")
else:
    print("working hours")   
#example3
k=5
l=9
print(k<l)
print(not(k<l))