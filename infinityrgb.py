import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.speed(11)

n=60
h=0
t.right(45)
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)

    t.circle(30)
    if 7 < i < 62:
        t.left(5)
    if 80 < i < 133:
        t.right(5)
    if i < 80:
        t.forward(10)
    else:
        t.forward(5)