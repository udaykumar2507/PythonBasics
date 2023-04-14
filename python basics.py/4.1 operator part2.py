#logical operator
#example1
a=13
b=45
print(a is b)
print( a is not b)
#example2
a1="tere naam"
if type(a1) is str:
    print("correct")
else:
    print("incorrect") 
#example 3
b1=45
if type(b1) is not str:
    print("correct")
else:
    print("incorrect")           
#MEMBERSHIP OPERATOR
#example1
a3="indian flag"
if "flag" in a3:
    print("correct")
else:
    print("incorrect")
#example2
a4=[1,2,3,4,5]        
if 6 in a4:
    print("correct")
else:
    print("incorrect")    
#