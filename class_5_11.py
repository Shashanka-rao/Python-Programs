x=[1,2,3]
y=x
x[1]= 99
x=[4,5,6]
print(id(x))
# z=x
# x[2]=10
# print(y)
print(x,y)

x=[1,2,3]
y=x
 
print(id(x))  #prints the memory address of x


def addj(x1):
    x1.append(4)

def dosomethin(z):
    z += 5
    # return z

x1=[1,2,3]
addj(x1)
print(x1)

y1=5
dosomethin(y1)
# y1 = dosomethin(y1)
print(y1)

x2=tuple(x)
print(x2)

x3=list(x2)
print(x3)

#dictionary

mydict={'name':'sandeep','age':20,'profession':'student','title':'saandy'}
print(mydict['title'])

# pgm
birthsays = { 'alice':'apr 1','bob':'mar 1','carol':'mar 4'}
while True:
    print('enter  NAME(blank to quit)')
    name=input()
    if name == ' ':
        break
    if name in birthsays:
        print(birthsays[name]+' is the birthday')
        break
    else:
        print('i dont have that name')
for k,v in birthsays.items():
    print(k,':',v)
print(birthsays.keys())
print(birthsays.values())