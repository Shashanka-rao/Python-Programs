mylist=[1,2,3,4,5]
mylist.insert(5,6)
print(mylist)
print(mylist.insert(100,99)==mylist.append(99))
del(mylist[5])
print(mylist)
mylist.remove(3)
print(mylist)
del(mylist[mylist.index(2)])
print(mylist)
mylist1=['cat','mat','Bat','Rat','SAT']  #ascii wise comparision
mylist1.sort()
print(mylist1)
mylist1.sort(reverse=True)
print(mylist1)
mylist1.sort(key= str.lower)

print(type((1,2,'hello')))

print(type([1,2,'hello']))

print(type(['hello',]))

print(type(('hello',)))

print(type(('hello')))

print(list((1,2,3)))

print(tuple([1,2,3]))


