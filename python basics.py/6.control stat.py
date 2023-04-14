#IF STATEMENT
#EXAMPLE1 (TO FIND THE GIVEN NUM IS EVEN OR ODD)
A=int(input("enter the num"))
if A%2==0:
    print("even")
else:
    print("odd")    
#EXAMPLE2(VOTING IS ELIGIBLE OR NOT)
age=int(input("enter the age:"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")    
#EXAMPLE 3(WRITE A PROGRAM TO FIND MAX BETWEEN TWO NUM) 
A1=int(input("enter the num"))
B1=int(input("enter the num"))
if A1>B1:
    print(A1,"IS MAX")
else:
    print(B1,"is max")
#EXAMPLE4 (WRITE A PROGRAM TO FIND MAX BETWEEN  THREE NUM )
A2=int(input("enter the num1"))
B2=int(input("enter the num2"))
C2=int(input("enter the num"))
if A2>B2  and A2>C2:
    print(A2,"is max")
elif B2>C2 and B2>C2:
    print(B2,"is max")
else:
    print(C2,"IS MAX") 
#EXAMPLE 5(WRITE A PROGRAM TO CHECK WHETHER A GIVEN NUM IS POSITIVE , NEGATIVEOR ZERO_)
N=int(input("enter the num"))
if (N<0):
    print("negative")
elif(N>0):
    print("positive")
else:
    print("zero")          
#EXAMPLE6( PROGRAM TO PRIN THE MIDDLE NUMBER)
A3=int(input("ENTER THE NUM:"))
B3=int(input("enter the num:"))
C3=int(input("enter the num"))
if A3<B3 and B3>C3:
    print(B3,"IS MIDDLE")
elif B3<A3 and A3>C3:
    print(A3,"is mid")
else:
    print(C3," is mid")    