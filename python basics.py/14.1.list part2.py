# all function revise
a=[]
n=int(input("enter the number"))
for i in range(n):
    x=input("enter the value")
    a.append(x)
#len
print("len function")
print(len(a))
#max
print("the max is")
print(max(a))
#min
print("min is")
print(min(a))
#count
print("the count is")
print(a.count("sansa"))
#index
print("index is")
print(a.index("sansa"))
#insert
print("insert")
a.insert(2,"ramsay")
print(a)
#remove
print("remove function")
a.remove("sansa")
print(a)
#reverse
print("reverse is")
a.reverse()
print(a)
#sort()
print("the sort is")
a.sort()
print(a)
#pop
print("pop is")
a.pop()
print(a)