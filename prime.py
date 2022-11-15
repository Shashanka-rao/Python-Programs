from itertools import count


num=400
print(0)
print(1)
for n in range(1,400):
    count=0
    for i in range(2,(n//2+1)):
        if(n%i==0):
            count=count+1
            break

    if(count==0 and n!=1):
        print("%d"%n,end=' ')
        
# flag=0
# start=100
# end=400
# for i in range(start,end):
#     start=start+1
#     if start%i==0 :



