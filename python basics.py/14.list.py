#list
a=["one","two","three"]
b=[1,2,3,4]
c=[1.2,2.2,3.5,6.5]
d=[1,"three",7.8,"four"]
#list slicing
a=["k","g","f",3]
print(a[0:])
print(a[:])
print(a[1:3])
print(a[:3])
#updating list in python
b=["n","t","r",10]
print(b)
print(b[1])
b[1]="sir"
print(b[1])
print(b)
#del list in python
c=["r","a","j","u"]
print(c)
del c[3]
print(c)
#transversal in list
a=["ram",10,"shyam",12.55]
for i in a:
    print("transvertse is",i)
#len func
a=[1,2,3,4,"shyam"]
print('length is',len(a))
#max func
a=["a","b","c","d"]
b=max(a)
print("max is",b)
#min func
a=['a','b','c','d']
b=min(a)
print("min is",b)
#append function
a=["a","b","c","d"]
a.append("terimeri")
print(a)
#count function
a=[1,2,3,4,5,4,4]
print(a.count(4))
#index fuunction
a=["star lrd","gamora","drags","rocket"]
print(a.index("star lrd"))
#insert function
a=["ujjjval","uday kumar","maurya","onion"]
c=a.insert(2,"anda biryani")
print(a)
#remove function()
a=["captain","iron man","thor","hulk","antman"]
a.remove("antman")
print(a)
#reverse function()
a=["war","gokul","honey","money"]
a.reverse()
print(a)
#sort function()
a=[9,8,7,6,5,4,3,2,1]
a.sort(reverse=False)
print(a)
#pop()
a=["ram","shyam","balram","gokul"]
a.pop()
print(a)
