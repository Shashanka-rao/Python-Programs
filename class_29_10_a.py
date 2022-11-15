import random



num=random.randint(0,100)
# num=num*10045
#num=int(num)
for x in range(0,10):
    guess=int(input("Entre the number: "))
    if(num<guess):
        print("guessed number is greater ,Try a Smaller number ")
    elif(num>guess):
        print("guessed number is Smaller ,Try a Greater number")
    else:
        print("WOOOHOOOOO U Won!!!!!")
        exit
print("Game Over")
print("number was "+str(num))