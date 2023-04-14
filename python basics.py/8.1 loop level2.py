#find the revers eof the given number
n=int(input("enter thenum"))
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
print(rev)
#to check whether a given mum is palindrome
n=int(input("enter the num"))
orig=n
rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
print(rev)
if rev==orig:
    print("palindrome")
else:
    print("not palindrome")  
#prime numbers
n=int(input("enter the num:"))
i=1
sum=0
while(i<=n):
    if n%i==0:
        sum+=1
    i+=1
if sum==2:
     print("prime number")
else:
    print("not prime number")
#factorial oif number
n=int(input('enter the num:'))
prod=1
while(n>1):
    prod=prod*n
    n-=1
print(prod)
#fibonaci series
n=int(input("enter the num"))
x=0
y=1
z=0
while(z<=n):
    x=y
    y=z
    z=x+y
    print(z)