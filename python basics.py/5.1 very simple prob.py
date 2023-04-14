#to exchaange values of two numbers
a=int(input("enter the num"))
b=int(input("enter the num"))
print(a)
print(b)
a,b=b,a
print(a)
print(b)
#write a program to accept total sales amount
sales=int(input("enter the sales:"))
n=int(input("enter the percentage"))
profit=(sales/100)*n
print("total sales",sales+profit)
