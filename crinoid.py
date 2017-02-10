##########################################draw crinoid
import turtle
turtle.speed(0)
#set beginning draw position (a,b) stalk curvature (h), initial orientation (o), pensize(p) and size (s)
a=85
b=-420
s=3 #(<5)
h=-4 #segment curvature (0-10)
p=1
o=0
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o)
turtle.fillcolor("grey")
turtle.pencolor("black")
turtle.pd()
turtle.pensize(p)

#draw stalk
#curve 1
for i in range(10):
        turtle.begin_fill()
        turtle.circle(s)
        turtle.end_fill()
        turtle.circle(s,180-(h*.5))
        turtle.left(90)
        turtle.pu()
        turtle.fd(s*.8)
        turtle.left(90)
        turtle.pd()
#curve 2
for i in range(12):
        turtle.begin_fill()
        turtle.circle(s)
        turtle.end_fill()
        turtle.circle(s,180+h)
        turtle.left(90)
        turtle.pu()
        turtle.fd(s*.8)
        turtle.left(90)
        turtle.pd()

#draw crinoid flower base
turtle.begin_fill()
turtle.circle(s*1.7)
turtle.end_fill()
turtle.circle(s*1.7,180)
turtle.left(90)
turtle.pu()
turtle.fd(s*.8)
turtle.left(180)
turtle.fd(s*4)
turtle.pd()


#draw crinoid flower head/feeding arms
n=60
for j in range(n):
        turtle.fd(s*10)
        turtle.left(360 // n + 180)
        turtle.fd(s*10)
	
	
turtle.ht()
input()
