#program tocount total vowel and constant
a=input("enter the value")
vowel=0
constant=0
for i in range(len(a)):
    if a[i]=="a"or a[i]=="e"or a[i]=="i"or a[i]=="o"or a[i]=="u":
        vowel+=1
    else:
        constant+=1 
print(vowel)
print(constant)
#STRING BUILTIN FUNCTION
#STRING BUILTIN FUNCTION
#len funcction
a="ram kumar"
print(len(a))
#capitalize 
a="struggle"
print(a.capitalize())
#find()
A="ram is going to market"
b="to"
A.find(b,0,len(a)-1)
#palindrome string
a=input("enter the string")
b=a[-1::-1]
if (a==b):
    print("palindrome string")
else:
    print("not palindrome string")
#isalnum
a="chutki123"
print(a.isalnum())
#isdigit
a="1234"
print(a.isdigit())
#isspace
a="    "
print(a.isspace())

