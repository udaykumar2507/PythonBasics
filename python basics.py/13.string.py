#strings in python
#strings are immutable
#initializing and printing a string
#example1
name="narayan"
print(name)
#example2
name="morthy"
for i in name:
    print(i)
#STRING OPERATORS
#concatenation operator
name1="tony"
name2="stark"
print(name1+name2)
#replication opertor
name1="debaba"
print(name1*100)
#membership operator
name="aquafina"
print("i" in name)
#comparison operator
name1="india"
name2="pakistan"
print(name1==name2)
print(name1!=name2)
#SLICING IN STRINGS
a="hello world"
print(a[4:-2])
a="Hello world"
print(a[6:],a[:6])
#REVERSE
a=input("enter string")
print(a[1::-1])
#another one
a=input("enter string")
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")