#write a program to sum of the digits
n=int(input("enter the num:"))
sum=0
while(n>0):
    sum=sum+(n%10)
    n=n//10
print(sum)
#write a program to find sum of square of digits
n=int(input("enter the num:"))
sum=0
while(n>0):
    sum=sum+(n%10)**2
    n=n//10
print(sum)
#sum of cube of digit of number
n=int(input("renetr the numebr")) 
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
print(sum)
#to check whether the given num is armstrong or not
n=int(input())
orig=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
print(sum)
if sum==orig:
    print("armstrong")
else:
    print("not armstrong")
#to print  the product of given number
n=int(input("enter the num;"))
prod=1
while(n>0):
    prod=prod*(n%10)
    n=n//10
print(prod)
