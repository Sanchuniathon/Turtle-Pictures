#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=200
b=-150
s=100
i=s
p=s*.01
h=35

import turtle
turtle.pu()
turtle.speed(0)
turtle.setposition(a,b)
turtle.pd()
turtle.pensize(p*3)
#draw coral (multipliers of i can be adjusted to tweak look of coral)
for i in [i*.3,i*.5,i,i*.9,i*.7,i*.45,i*.3]:
        turtle.setheading(h)
        turtle.pencolor("black")
        turtle.fillcolor("brown")
        turtle.fd(i)
        turtle.begin_fill()
        turtle.circle(s*.1,540)
        turtle.left(90)
        turtle.fd(s*.1)
        turtle.dot(s*.2)
        turtle.left(180)
        turtle.fd(s*.1)
        turtle.left(90)
        turtle.setposition(a,b)
        turtle.end_fill()
        h=h+14

turtle.ht()
turtle.pu()
input()
