#DIFFRENCE 1
list=[1,"black","panther","america"]
tupules=(1,"black","panther","america")
#DIFFRENCE2
#list are mutable tuples are immutable
#DIFFRENCE 3
#LIST OCCUPIES MORE SPACE AND TAKE MORE TIME THAN TUPLE



#DECLARE A TUPLE IN PYTHON
'''TUPLE1=() THIS IS AN EMPTY TUPLE
TUPLE=(VAL1,VAL2,VAL3...)
TUPLE1=(2)  THIS IS NOT A TUPLE IT IS A INTEGER CLASS  
TUPLE1=(2,) IT IS A TUPLE'''
#CREATING TUPLES FROM STRING
t1=tuple("world")
print(t1)
#cerating tuples from list
t1=tuple([1,2,3,4,5])
print(t1)
#transversing a tuple
tuple1=(1,2,3,4)
for i in tuple1:
    print(i)
#joining tuples
tup1=(1,2,3)
tup2=("ben","ten")
print(tup1+tup2)
#repeating or replecating tuples
tuple1=(1,2,3)
tup2=tuple1*3
print(tup2)
#slicing a tuple
tuple1=(1,2,3,4,6)
tupl2=tuple1[2:-1]
print(tupl2)
