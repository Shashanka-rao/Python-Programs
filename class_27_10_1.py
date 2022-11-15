for i in range(1,101):
    if i%3==0 and i%5==0:
        print('fizz buzz')
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

# another pgm
flag=0
for i in range(1,101):
    flag=0
    if not i%3:
        print('fizz')
        flag=1
    if not i%5:
        print('buzz')
        flag=1

    if not flag:
        print(i)