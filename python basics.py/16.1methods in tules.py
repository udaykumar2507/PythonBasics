#len
tup=(1,2,3,4,5)
print(len(tup))
#max
tup=(1,2,3,45)
print(max(tup))
#min
tup=(23,4,5,6,878)
print(min(tup))
#index
tup=(2,4,6,8,9)
print(tup.index(6))
#count
tup=(2,3,5,5,6)
print(tup.count(5))
#changing tupules values
phase1=("iron man","incredible hulk",'thor',"iron man2","captain america")
print(phase1)
y=list(phase1)
y[0]="IRON MAN"
phase1=tuple(y)
print(y)
#check if exist
x=("thor the dark world","age of ultron","ironman3")
y="age of ultron"
if y in x:
    print("yes")
else:
    print("no")
#adding element5 in a tuple is not possible
phase3=("guardian of galaxy","thor ragnarok")
y=list(phase3)
y.append("homecoming")
phase1=tuple(y)
print(phase1)
#del statement (we cannot delete a eleemnt in a tuple but we can del entire tuple)
tup1=(1,2,3,4,5)
del(tup1)
#this will show error
#print(tup1)    

