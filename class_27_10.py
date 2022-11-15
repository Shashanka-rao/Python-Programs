from cgi import print_environ


myList=[1,2,3,6]
# multiplying list
print(myList*3)
# initializing variables
a,b,c,d=myList
print(a,b,c,d)
for i in myList:
    print(i,end=' ')
print(" ")
# appending
myList.append(999)
# deleting
del(myList[2])
for i in myList:
    print(i,end=' ')

strfile="hello world"
mydict={}
words=strfile.split('')
for word in words:
    if word in mydict:
        mydict[word]+=1
    else:
        mydict[word]=1
print(mydict)