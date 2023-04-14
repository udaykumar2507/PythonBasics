#FUNCTION =SUBPROGRAM=PART OF PROGRAM
#EXAMPLE(to print helo world using function)
def message():
    print("hello world")
message()
#example 2(to add two number using function)
def add():
    a=int(input("enter the number"))
    b=int(input("enter the number" ))
    c=a+b
    print(c)
add()
#FUNCTION ARGUMENTS/PARAMETRS
#TO PRINT SUM
def sum(a,b):
    print(a+b)
sum(4,5)
def sum2(a,b):
    c=a+b
    print(c)
a=int(input("enter the num"))
b=int(input("enter the nmum"))
sum2(a,b)
#WITHOUT ARGUMENT AND WITH ARGUMENT
#to find given num is odd or even
#without argument
def oddeven():
    n=int(input("enter the number"))
    if n%2==0:
        print("even")
    else:
        print("odd")
oddeven()
#with argument
def oddeven1(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
oddeven1(5)
'''NO ARGUMENT NO REURN
   WITH ARGUMENT NO RETURN
   NO ARGUMENT WITH RETURN
   WITH ARGUMENT WITH RETURN'''
#NANR
def add():
    a=10
    b=10
    print(a+b)
add()
#WANR
def add(a,b):
    print(a+b)
add(5,6)
#NAWR
def add():
    a=10
    b=10
    c=a+b
    print(c)
    return c
x=add()
print(x)
#WAWR
def add(a,b):
    c=a+b
    print(c)
    return c
x=add(5,6)
print(x)    
#DEFAULT ARGUMENT 
def add(a,b,c=10):
    d=a+b+c
    print(d)
add(4,5)
