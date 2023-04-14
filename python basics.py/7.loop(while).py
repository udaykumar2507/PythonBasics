#while programming 
#WRITE A PROGRAM TO PRINT FROM 1 TO 10
i=1
while(i<=10):
    print(i)
    i+=1
#WRITE A PROGRAM TO PRINT FROM 1 TO N
n=int(input('enter the num you want to print'))
I=1
while (I<=n):
    print(I)
    I+=1
#WRITE A PRIGRAM TO PRINT FROM N TO 1
n=int(input("enter the num in reverse:"))
i=n
while(i>=1):
    print(i)
    i-=1
#write a program to sum of integers
n=int(input("enter the num to sum"))
sum=0
i=1
while(i<=n):
    print(i)
    sum+=i
    i+=1
print(sum)

#write a program to print the square
n=int(input("enter the number to print sum of square"))
i=1
sum=0
while(i<=n):
    sum+=i**2
    i+=1
    print(sum)
#print even number from 1 to n
n=int(input("enter the num print  1 to n in even"))
i=1
while(i<=n):
    if i%2==0:
        print(i)
    i+=1
#print  aprogram to sum of cubes
n=int(input("enter the num"))
i=1
sum=0
while(i<=n):
    sum+=i*i*i
    i+=1
print(sum)    
#print program to sum of even numbers
n=int(input("enetr the num:"))
i=1
sum=0
while(i<=n):
    if i%2==0:
        sum+=i
    i+=1
print(sum)
#print program to find sum of first n even number
n=int(input('enetr the number of first n  even num'))
sum=0
count=0
i=1
while(count<n):
    if (i%2==0):
        sum+=i
        count+=1
    i+=1
print(sum)    
#printfrom 10 to 1
i=10
while(i>=1):
    print(i)
    i-=1
    