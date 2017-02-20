#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=260
b=-130
s=25
m=s
p=s*.05
h=0
import turtle
turtle.speed(0)
turtle.pu()
###draw ammonite

#draw ammonite spiral
turtle.setposition(a,b)
turtle.setheading(h)
turtle.pd()
turtle.color("black","#996600")
turtle.pensize(s*.1)
turtle.begin_fill()
turtle.fd(s*.4)
for s in [s,s,s*.9,s*.8,s*.7,s*.6,s*.5,s*.4,s*.3,s*.2,s*.2,s*.1]:
        turtle.circle(s,60)
        turtle.pensize(s*.2)
        turtle.left(90)
        turtle.fd(0.2*s)
        turtle.left(180)
        turtle.fd(0.2*s)
        turtle.left(90)
        turtle.pensize(s*.1)
s=m
#spiral back out
turtle.right(180)
for s in [s*-.1,s*-.2,s*-.2,s*-.3,s*-.4,s*-.5,s*-.6]:
        turtle.circle(s,60)
s=m

#draw tentacles and hood
turtle.pensize(p*1.5)
turtle.left(90)
turtle.fd(s*.6)
turtle.left(150)
turtle.fd(s*.8)

#finish shell
turtle.circle(s*-.7,70)
turtle.end_fill()
turtle.color("black","#ff9933")
turtle.begin_fill()
turtle.left(180)
turtle.circle(s*.7,70)
turtle.pensize(p)
turtle.right(0)
#draw tentacles/arms
turtle.fd(s*1.4)
for j in [0,1,2,3]:
        turtle.left(170)
        turtle.fd(s*.7)
        turtle.right(168)
        turtle.fd(s*.7)

#draw siphon tube
turtle.pensize(p*.4)
turtle.circle(s*.06,540)
turtle.left(90)
turtle.fd(s*.06)
turtle.dot(s*.12)
turtle.left(180)
turtle.fd(s*.06)
turtle.left(90)
turtle.pensize(p*.6)
turtle.fd(s*.7)
turtle.pensize(p*.8)
turtle.setposition(a,b)
turtle.end_fill()

#draw eye
turtle.pu()
c=a-(s*.15)
d=b+(s*.25)
turtle.setposition(c,d)
turtle.pendown()
turtle.pensize(p*.6)
turtle.color("black","white")
turtle.begin_fill()
turtle.circle(s*.12,None,5)
turtle.end_fill()
turtle.pu()
turtle.color("black","black")
turtle.left(90)
turtle.fd(s*.1)
turtle.right(10)
turtle.pd()
turtle.begin_fill()
turtle.pensize(p*.2)
turtle.circle(s*.05)
turtle.end_fill()


turtle.pu()
turtle.ht()
input()
