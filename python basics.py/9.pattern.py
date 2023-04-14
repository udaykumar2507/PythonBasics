#to print pyramid in incresing order
n=int(input("enter teh number"))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1
    print()
    i+=1
#to print star with gap in half pyramid
n=int(input("enter the number"))
i=1
while(i<=n):
    j=1
    while(j<=n-i):
        print(" ",end=" ")
        j+=1
    k=1
    while(k<=i):
        print("*",end=" ")
        k+=1
    print()
    i+=1
#to print pyramid 
n=int(input("entr the number"))
i=1
k=1
while(i<=n):
    j=1
    while(j<=n-i):
        print(" ",end="")
        j+=1
    b=1
    while(b<=k):
        print("*",end="")
        b+=1
    k+=2
    print()
    i+=1        
# to print pyramid with number(by pinting diffrent varible we can use this)
n=int(input("entr the number"))
i=1
k=1
while(i<=n):
    j=1
    while(j<=n-i):
        print(" ",end="")
        j+=1
    b=1
    while(b<=k):
        print(i,end="")
        b+=1
    k+=2
    print()
    i+=1   
     
    