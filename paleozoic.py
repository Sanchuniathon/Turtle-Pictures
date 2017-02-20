#establish basic premises and environment
import turtle

turtle.hideturtle()
turtle.tracer(12345)
turtle.pu()
turtle.setup(1500,1000)

#draw ocean backdrop
turtle.setposition(-750,500)

for i in ["#33bbff","#1ab2ff","#00aaff","#0099e6","#0088cc","#0077b3","#006699","#005580"]:
        turtle.fillcolor(i)
        turtle.begin_fill()
        turtle.fd(1500)
        turtle.right(90)
        turtle.fd(100)
        turtle.right(90)
        turtle.fd(1500)
        turtle.end_fill()
        turtle.right(180)



#draw seafloor
turtle.setheading(0)
turtle.setposition(-750,-100)
turtle.fillcolor("#B8860B")
turtle.begin_fill()
turtle.pd()
turtle.left(223)
turtle.circle(1200,None,4)
turtle.end_fill()
turtle.pu()


##########################################draw crinoid 1a
#set beginning draw position (a,b) stalk curvature (h), initial orientation (o), pensize(p) and size (s)
a=85
b=-420
s=3 #(<5)
h=-4 #segment 2 curvature (0-10)
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


############################################### Draw ammonite hiding behind coral
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=260
b=-130
s=25
m=s
p=s*.05
h=0
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


################## Draw coral 1
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=200
b=-150
s=100
i=s
p=s*.01
h=35

import turtle
import random
turtle.setposition(a,b)
turtle.pd()
turtle.pensize(p*3)
#draw coral
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
turtle.pu()

################## Draw coral 2
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=300
b=-250
s=80
i=s
p=s*.01
h=35

import turtle
import random
turtle.setposition(a,b)
turtle.pd()
turtle.pensize(p*3)
#draw coral
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

turtle.pu()


################## Draw coral 3
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=425
b=-270
s=200
i=s
p=s*.01
h=35

import turtle
import random
turtle.setposition(a,b)
turtle.pd()
turtle.pensize(p*3)
#draw coral
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

turtle.pu()


################## Draw coral 4
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=-175
b=-130
s=60
i=s
p=s*.01
h=35

import turtle
import random
turtle.setposition(a,b)
turtle.pd()
turtle.pensize(p*3)
#draw coral
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

turtle.pu()

##################Draw Spiriferid brachiopod 1
#set beginning draw position (a,b) initial orientation (o) and size (s)
a=195
b=-120
o=310
l=o
s=20
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o)
turtle.fillcolor("#333300")
turtle.pencolor("#666633")
turtle.pensize(s*.1)
turtle.begin_fill()
turtle.pd()

#draw outside edge double partial circle
turtle.circle(s,40)

#draw outer wing nub on right
turtle.circle(-s*.08,160)

#draw ruffled edge on right
for i in range(5):
        turtle.setheading(l-45)
        turtle.circle(-s*0.03,160)
        turtle.circle(s*.03,160)
l=o

#mark position for base line along shell
c=turtle.xcor()
d=turtle.ycor()

#draw central curve across on right
turtle.setheading(l+170)
turtle.circle(-s*.5,60)
turtle.end_fill()
l=o


turtle.pu()

#start other side of shell

turtle.begin_fill()
turtle.pd()
turtle.setposition(a,b)


#draw outside edge double partial circle 2
turtle.left(295)
turtle.circle(s,-40)


#draw outer wing nub on left
turtle.setheading(l-180)
turtle.circle(s*.08,160)
l=o
#draw ruffled edge on left
for i in range(5):
        turtle.setheading(o-90)
        turtle.circle(s*.03,160)
        turtle.circle(-s*0.03,160)
l=o
#mark end position for base line along shell
e=turtle.xcor()
f=turtle.ycor()

#draw central line across on left
turtle.setheading(o-310)
turtle.circle(s*.5,60)
turtle.setposition(a,b)
turtle.end_fill()

#finish base line along shell
turtle.begin_fill()
turtle.fillcolor("#4d4d00")
turtle.pu()
turtle.setposition(c,d)
turtle.pd()
turtle.setposition(e,f)
turtle.end_fill()

###########draw seaweed 1a
#set starting point
x=265 #start coordinate x
y=-150 #start coordinate  y
h=25 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()
###########draw seaweed 1
#set starting point
x=220 #start coordinate x
y=-160 #start coordinate  y
h=25 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()

###########draw seaweed 2
#set starting point
x=260 #start coordinate x
y=-190 #start coordinate  y
h=22 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()

###########draw seaweed 3
#set starting point
x=30 #start coordinate x
y=-165 #start coordinate  y
h=25 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()

###########draw seaweed 4
#set starting point
x=-200 #start coordinate x
y=-200 #start coordinate  y
h=17 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()

###########draw seaweed 5
#set starting point
x=-500 #start coordinate x
y=-220 #start coordinate  y
h=35 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()
########## trilobite bottom right (:{{{D
#set beginning draw position (a,b) initial orientation (o), pensize(p) and size (s)
a=500
b=-290
o=110
s=7
l=s
p=s*.1
import turtle
turtle.speed(0)
turtle.pu()
turtle.pensize(p)
turtle.setposition(a,b)
turtle.setheading(o)
turtle.pd()

#draw top of head
turtle.circle(s*.6,45)
turtle.right(75)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*1.2,140)
p=s*.1

#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        turtle.fillcolor("grey")
        turtle.begin_fill()

        #start side edge
        turtle.right(75)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90) 
        turtle.circle(s*.6,70)
        turtle.left(125)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80) 
        turtle.fd(s*.3)
        turtle.right(40)
        turtle.circle(-s,110)

        #draw central spine
        turtle.left(140) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(-s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(s*.4,45)
        turtle.right(90)
        turtle.circle(s,110)
        
        turtle.left(45)
        turtle.fd(s*.6)
        turtle.left(70)

#draw tail section
#rear spine
turtle.begin_fill()
turtle.right(150)
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*4,70)
p=s*.1
turtle.pensize(p)
#connecting tail 
turtle.right(120)
turtle.circle(s,90)
turtle.end_fill()

######################################left side now finished repeat on right, backwards
s=l
p=s*.1
turtle.pensize(p)
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o-180)
turtle.pd()

#draw top of head
turtle.circle(-s*.6,45)
turtle.right(75+180+30)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(-s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90+180)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(-s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*1.2,140)
p=s*.1
#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        #turtle.fillcolor("brown")
        turtle.begin_fill()
        #start side edge
        turtle.right(75+180+30)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90+180) 
        turtle.circle(-s*.6,70)
        turtle.left(125+110)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80+200) 
        turtle.fd(s*.3)
        turtle.right(40+100+180)
        turtle.circle(s,110)
        
        #draw central spine
        turtle.left(140+80) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140-100)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(-s*.4,45)
        turtle.right(90+180)
        turtle.circle(-s,110)
        
        turtle.left(45+180+90)
        turtle.fd(s*.6)
        turtle.left(70+180+40)
#draw tail section
turtle.begin_fill()
turtle.right(150+60)
#rear spine
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(-s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*4,70)
p=s*.1
#connecting tail
turtle.pensize(p)
turtle.right(120+120)
turtle.circle(-s,90)
turtle.end_fill()

#footprints
turtle.pu()
turtle.setposition(a,b)
turtle.left(105)
turtle.fd(s*8)
turtle.right(65)
turtle.fd(s*2)
for i in range (15):
        turtle.dot(s*.5)
        turtle.left(130)
        turtle.fd(s*4)
        turtle.dot(s*.5)
        turtle.right(130)
        turtle.fd(s*4)

turtle.pu()

###########draw seaweed 6
#set starting point
x=550 #start coordinate x
y=-370 #start coordinate  y
h=90 #seaweed draw circle radius
k=h
p=h*.2
b=90 #seaweed draw start angle
turtle.pu()
turtle.setposition(x,y)
turtle.pd()

turtle.pensize(p)              #draw green leaves
for b in [b,b-30,b-60]:
        turtle.pencolor("green")
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k


turtle.pensize(p*.25)               #now draw inner black line
b=90
for b in [b,b-30,b-60]:
        turtle.pencolor("black")
        
        turtle.pd()
        turtle.setheading(b)        
        for h in [h,-h,h*.6]:
                turtle.circle(h,60)
        turtle.pu()
        turtle.setposition(x,y)
        h=k
turtle.pu()
########## trilobite bottom right 2 (:{{{D
#set beginning draw position (a,b) initial orientation (o), pensize(p) and size (s)
a=430
b=-350
o=100
s=7
l=s
p=s*.1
import turtle
turtle.speed(0)
turtle.pu()
turtle.pensize(p)
turtle.setposition(a,b)
turtle.setheading(o)
turtle.pd()

#draw top of head
turtle.circle(s*.6,45)
turtle.right(75)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*1.2,140)
p=s*.1

#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        turtle.fillcolor("grey")
        turtle.begin_fill()

        #start side edge
        turtle.right(75)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90) 
        turtle.circle(s*.6,70)
        turtle.left(125)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80) 
        turtle.fd(s*.3)
        turtle.right(40)
        turtle.circle(-s,110)

        #draw central spine
        turtle.left(140) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(-s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(s*.4,45)
        turtle.right(90)
        turtle.circle(s,110)
        
        turtle.left(45)
        turtle.fd(s*.6)
        turtle.left(70)

#draw tail section
#rear spine
turtle.begin_fill()
turtle.right(150)
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*4,70)
p=s*.1
turtle.pensize(p)
#connecting tail 
turtle.right(120)
turtle.circle(s,90)
turtle.end_fill()


######################################left side now finished repeat on right, backwards
s=l
p=s*.1
turtle.pensize(p)
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o-180)
turtle.pd()

#draw top of head
turtle.circle(-s*.6,45)
turtle.right(75+180+30)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(-s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90+180)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(-s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*1.2,140)
p=s*.1
#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        #turtle.fillcolor("brown")
        turtle.begin_fill()
        #start side edge
        turtle.right(75+180+30)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90+180) 
        turtle.circle(-s*.6,70)
        turtle.left(125+110)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80+200) 
        turtle.fd(s*.3)
        turtle.right(40+100+180)
        turtle.circle(s,110)
        
        #draw central spine
        turtle.left(140+80) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140-100)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(-s*.4,45)
        turtle.right(90+180)
        turtle.circle(-s,110)
        
        turtle.left(45+180+90)
        turtle.fd(s*.6)
        turtle.left(70+180+40)
#draw tail section
turtle.begin_fill()
turtle.right(150+60)
#rear spine
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(-s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*4,70)
p=s*.1
#connecting tail
turtle.pensize(p)
turtle.right(120+120)
turtle.circle(-s,90)
turtle.end_fill()

#footprints
turtle.pu()
turtle.setposition(a,b)
turtle.left(105)
turtle.fd(s*8)
turtle.right(65)
turtle.fd(s*2)
for i in range (15):
        turtle.dot(s*.5)
        turtle.left(130)
        turtle.fd(s*4)
        turtle.dot(s*.5)
        turtle.right(130)
        turtle.fd(s*4)

turtle.pu()

########## trilobite bottom left (:{{{D
#set beginning draw position (a,b) initial orientation (o), pensize(p) and size (s)
a=-550
b=-310
o=90
s=13
l=s
p=s*.1
import turtle
turtle.speed(0)
turtle.pu()
turtle.pensize(p)
turtle.setposition(a,b)
turtle.setheading(o)
turtle.pd()

#draw top of head
turtle.circle(s*.6,45)
turtle.right(75)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*1.2,140)
p=s*.1

#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        turtle.fillcolor("grey")
        turtle.begin_fill()

        #start side edge
        turtle.right(75)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90) 
        turtle.circle(s*.6,70)
        turtle.left(125)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80) 
        turtle.fd(s*.3)
        turtle.right(40)
        turtle.circle(-s,110)

        #draw central spine
        turtle.left(140) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(-s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(s*.4,45)
        turtle.right(90)
        turtle.circle(s,110)
        
        turtle.left(45)
        turtle.fd(s*.6)
        turtle.left(70)

#draw tail section
#rear spine
turtle.begin_fill()
turtle.right(150)
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*4,70)
p=s*.1
turtle.pensize(p)
#connecting tail 
turtle.right(120)
turtle.circle(s,90)
turtle.end_fill()

######################################left side now finished repeat on right, backwards
s=l
p=s*.1
turtle.pensize(p)
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o-180)
turtle.pd()

#draw top of head
turtle.circle(-s*.6,45)
turtle.right(75+180+30)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(-s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90+180)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(-s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*1.2,140)
p=s*.1
#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        #turtle.fillcolor("brown")
        turtle.begin_fill()
        #start side edge
        turtle.right(75+180+30)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90+180) 
        turtle.circle(-s*.6,70)
        turtle.left(125+110)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80+200) 
        turtle.fd(s*.3)
        turtle.right(40+100+180)
        turtle.circle(s,110)
        
        #draw central spine
        turtle.left(140+80) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140-100)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(-s*.4,45)
        turtle.right(90+180)
        turtle.circle(-s,110)
        
        turtle.left(45+180+90)
        turtle.fd(s*.6)
        turtle.left(70+180+40)
#draw tail section
turtle.begin_fill()
turtle.right(150+60)
#rear spine
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(-s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*4,70)
p=s*.1
#connecting tail
turtle.pensize(p)
turtle.right(120+120)
turtle.circle(-s,90)
turtle.end_fill()

#footprints
turtle.pu()
turtle.setposition(a,b)
turtle.left(105)
turtle.fd(s*8)
turtle.right(65)
turtle.fd(s*2)
for i in range (10):
        turtle.dot(s*.5)
        turtle.left(130)
        turtle.fd(s*4)
        turtle.dot(s*.5)
        turtle.right(130)
        turtle.fd(s*4)

###################################### Draw coral 5 (large bottom right spirifirid coral)
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=-400
b=-480
s=300
i=s
p=s*.01
h=35

import turtle
import random
turtle.setposition(a,b)
turtle.pd()
turtle.pensize(p*3)
#draw coral
for i in [i*.3,i*.5,i,i*1.3,i*1.2,i*.8,i*.3]:
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
        h=h+12

turtle.pu()

##################Draw Spiriferid brachiopod 2
#set beginning draw position (a,b) initial orientation (o) and size (s)
a=-420
b=-400
o=260
l=o
s=50
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o)
turtle.fillcolor("#333300")
turtle.pencolor("#666633")
turtle.pensize(s*.03)
turtle.begin_fill()
turtle.pd()

#draw outside edge double partial circle
turtle.circle(s,40)

#draw outer wing nub on right
turtle.circle(-s*.08,160)

#draw ruffled edge on right
for i in range(5):
        turtle.setheading(l-45)
        turtle.circle(-s*0.03,160)
        turtle.circle(s*.03,160)
l=o

#mark position for base line along shell
c=turtle.xcor()
d=turtle.ycor()

#draw central curve across on right
turtle.setheading(l+170)
turtle.circle(-s*.5,60)
turtle.end_fill()
l=o


turtle.pu()

#start other side of shell

turtle.begin_fill()
turtle.pd()
turtle.setposition(a,b)


#draw outside edge double partial circle 2
turtle.left(295)
turtle.circle(s,-40)


#draw outer wing nub on left
turtle.setheading(l-180)
turtle.circle(s*.08,160)
l=o
#draw ruffled edge on left
for i in range(5):
        turtle.setheading(o-90)
        turtle.circle(s*.03,160)
        turtle.circle(-s*0.03,160)
l=o
#mark end position for base line along shell
e=turtle.xcor()
f=turtle.ycor()

#draw central line across on left
turtle.setheading(o-310)
turtle.circle(s*.5,60)
turtle.setposition(a,b)
turtle.end_fill()

#finish base line along shell
turtle.begin_fill()
turtle.fillcolor("#4d4d00")
turtle.pu()
turtle.setposition(c,d)
turtle.pd()
turtle.setposition(e,f)
turtle.end_fill()

turtle.pu()

##################Draw Spiriferid brachiopod 3
#set beginning draw position (a,b) initial orientation (o) and size (s)
a=-400
b=-360
o=280
l=o
s=58
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o)
turtle.fillcolor("#333300")
turtle.pencolor("#666633")
turtle.pensize(s*.03)
turtle.begin_fill()
turtle.pd()

#draw outside edge double partial circle
turtle.circle(s,40)

#draw outer wing nub on right
turtle.circle(-s*.08,160)

#draw ruffled edge on right
for i in range(5):
        turtle.setheading(l-45)
        turtle.circle(-s*0.03,160)
        turtle.circle(s*.03,160)
l=o

#mark position for base line along shell
c=turtle.xcor()
d=turtle.ycor()

#draw central curve across on right
turtle.setheading(l+170)
turtle.circle(-s*.5,60)
turtle.end_fill()
l=o


turtle.pu()

#start other side of shell

turtle.begin_fill()
turtle.pd()
turtle.setposition(a,b)


#draw outside edge double partial circle 2
turtle.left(295)
turtle.circle(s,-40)


#draw outer wing nub on left
turtle.setheading(l-180)
turtle.circle(s*.08,160)
l=o
#draw ruffled edge on left
for i in range(5):
        turtle.setheading(o-90)
        turtle.circle(s*.03,160)
        turtle.circle(-s*0.03,160)
l=o
#mark end position for base line along shell
e=turtle.xcor()
f=turtle.ycor()

#draw central line across on left
turtle.setheading(o-310)
turtle.circle(s*.5,60)
turtle.setposition(a,b)
turtle.end_fill()

#finish base line along shell
turtle.begin_fill()
turtle.fillcolor("#4d4d00")
turtle.pu()
turtle.setposition(c,d)
turtle.pd()
turtle.setposition(e,f)
turtle.end_fill()

turtle.pu()

##################Draw Spiriferid brachiopod 4
#set beginning draw position (a,b) initial orientation (o) and size (s)
a=12
b=-250
o=0
l=o
s=32
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o)
turtle.fillcolor("#333300")
turtle.pencolor("#666633")
turtle.pensize(s*.03)
turtle.begin_fill()
turtle.pd()

#draw outside edge double partial circle
turtle.circle(s,40)

#draw outer wing nub on right
turtle.circle(-s*.08,160)

#draw ruffled edge on right
for i in range(5):
        turtle.setheading(l-45)
        turtle.circle(-s*0.03,160)
        turtle.circle(s*.03,160)
l=o

#mark position for base line along shell
c=turtle.xcor()
d=turtle.ycor()

#draw central curve across on right
turtle.setheading(l+170)
turtle.circle(-s*.5,60)
turtle.end_fill()
l=o


turtle.pu()

#start other side of shell

turtle.begin_fill()
turtle.pd()
turtle.setposition(a,b)


#draw outside edge double partial circle 2
turtle.left(295)
turtle.circle(s,-40)


#draw outer wing nub on left
turtle.setheading(l-180)
turtle.circle(s*.08,160)
l=o
#draw ruffled edge on left
for i in range(5):
        turtle.setheading(o-90)
        turtle.circle(s*.03,160)
        turtle.circle(-s*0.03,160)
l=o
#mark end position for base line along shell
e=turtle.xcor()
f=turtle.ycor()

#draw central line across on left
turtle.setheading(o-310)
turtle.circle(s*.5,60)
turtle.setposition(a,b)
turtle.end_fill()

#finish base line along shell
turtle.begin_fill()
turtle.fillcolor("#4d4d00")
turtle.pu()
turtle.setposition(c,d)
turtle.pd()
turtle.setposition(e,f)
turtle.end_fill()

turtle.pu()

##################Draw Spiriferid brachiopod 4
#set beginning draw position (a,b) initial orientation (o) and size (s)
a=-350
b=-340
o=290
l=o
s=32
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o)
turtle.fillcolor("#333300")
turtle.pencolor("#666633")
turtle.pensize(s*.03)
turtle.begin_fill()
turtle.pd()

#draw outside edge double partial circle
turtle.circle(s,40)

#draw outer wing nub on right
turtle.circle(-s*.08,160)

#draw ruffled edge on right
for i in range(5):
        turtle.setheading(l-45)
        turtle.circle(-s*0.03,160)
        turtle.circle(s*.03,160)
l=o

#mark position for base line along shell
c=turtle.xcor()
d=turtle.ycor()

#draw central curve across on right
turtle.setheading(l+170)
turtle.circle(-s*.5,60)
turtle.end_fill()
l=o


turtle.pu()

#start other side of shell

turtle.begin_fill()
turtle.pd()
turtle.setposition(a,b)


#draw outside edge double partial circle 2
turtle.left(295)
turtle.circle(s,-40)


#draw outer wing nub on left
turtle.setheading(l-180)
turtle.circle(s*.08,160)
l=o
#draw ruffled edge on left
for i in range(5):
        turtle.setheading(o-90)
        turtle.circle(s*.03,160)
        turtle.circle(-s*0.03,160)
l=o
#mark end position for base line along shell
e=turtle.xcor()
f=turtle.ycor()

#draw central line across on left
turtle.setheading(o-310)
turtle.circle(s*.5,60)
turtle.setposition(a,b)
turtle.end_fill()

#finish base line along shell
turtle.begin_fill()
turtle.fillcolor("#4d4d00")
turtle.pu()
turtle.setposition(c,d)
turtle.pd()
turtle.setposition(e,f)
turtle.end_fill()

turtle.pu()

############################################### Draw ammonite 1
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=-300
b=0
s=100
m=s
p=s*.05
h=340
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

############################################### Draw ammonite 2
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=-470
b=200
s=55
m=s
p=s*.05
h=350
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

############################################### Draw ammonite 3
#Set initial location (a,b), size (s), pensize(p),and orientation(h)
a=-560
b=55
s=35
m=s
p=s*.05
h=330
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

########## trilobite central (:{{{D
#set beginning draw position (a,b) initial orientation (o), pensize(p) and size (s)
a=-150
b=-200
o=220
s=5
l=s
p=s*.1
import turtle
turtle.speed(0)
turtle.pu()
turtle.pensize(p)
turtle.setposition(a,b)
turtle.setheading(o)
turtle.pd()

#draw top of head
turtle.circle(s*.6,45)
turtle.right(75)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*1.2,140)
p=s*.1

#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        turtle.fillcolor("grey")
        turtle.begin_fill()

        #start side edge
        turtle.right(75)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90) 
        turtle.circle(s*.6,70)
        turtle.left(125)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80) 
        turtle.fd(s*.3)
        turtle.right(40)
        turtle.circle(-s,110)

        #draw central spine
        turtle.left(140) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(-s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(s*.4,45)
        turtle.right(90)
        turtle.circle(s,110)
        
        turtle.left(45)
        turtle.fd(s*.6)
        turtle.left(70)

#draw tail section
#rear spine
turtle.begin_fill()
turtle.right(150)
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*4,70)
p=s*.1
turtle.pensize(p)
#connecting tail 
turtle.right(120)
turtle.circle(s,90)
turtle.end_fill()

######################################left side now finished repeat on right, backwards
s=l
p=s*.1
turtle.pensize(p)
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o-180)
turtle.pd()

#draw top of head
turtle.circle(-s*.6,45)
turtle.right(75+180+30)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(-s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90+180)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(-s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*1.2,140)
p=s*.1
#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        #turtle.fillcolor("brown")
        turtle.begin_fill()
        #start side edge
        turtle.right(75+180+30)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90+180) 
        turtle.circle(-s*.6,70)
        turtle.left(125+110)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80+200) 
        turtle.fd(s*.3)
        turtle.right(40+100+180)
        turtle.circle(s,110)
        
        #draw central spine
        turtle.left(140+80) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140-100)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(-s*.4,45)
        turtle.right(90+180)
        turtle.circle(-s,110)
        
        turtle.left(45+180+90)
        turtle.fd(s*.6)
        turtle.left(70+180+40)
#draw tail section
turtle.begin_fill()
turtle.right(150+60)
#rear spine
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(-s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*4,70)
p=s*.1
#connecting tail
turtle.pensize(p)
turtle.right(120+120)
turtle.circle(-s,90)
turtle.end_fill()

#footprints
turtle.pu()
turtle.setposition(a,b)
turtle.left(105)
turtle.fd(s*8)
turtle.right(65)
turtle.fd(s*2)
for i in range (10):
        turtle.dot(s*.5)
        turtle.left(127)
        turtle.fd(s*4)
        turtle.dot(s*.5)
        turtle.right(130)
        turtle.fd(s*4)

##########################################draw crinoid 1
#set beginning draw position (a,b) stalk curvature (h), initial orientation (o), pensize(p) and size (s)
a=-620
b=-160
s=2 #(<5)
h=10 #segment 2 curvature (0-10)
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


#draw crinoid flower head
n=60
for j in range(n):
        turtle.fd(s*10)
        turtle.left(360 // n + 180)
        turtle.fd(s*10)

##########################################draw crinoid 2
#set beginning draw position (a,b) stalk curvature (h), initial orientation (o), pensize(p) and size (s)
a=620
b=-490
s=4 #(<5)
h=7 #segment 2 curvature (0-10)
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


#draw crinoid flower head
n=60
for j in range(n):
        turtle.fd(s*10)
        turtle.left(360 // n + 180)
        turtle.fd(s*10)

##########################################draw crinoid 3
#set beginning draw position (a,b) stalk curvature (h), initial orientation (o), pensize(p) and size (s)
a=200
b=-300
s=3 #(<5)
h=12 #segment 2 curvature (0-10)
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


#draw crinoid flower head
n=60
for j in range(n):
        turtle.fd(s*10)
        turtle.left(360 // n + 180)
        turtle.fd(s*10)

########## trilobite near crinoid (:{{{D
#set beginning draw position (a,b) initial orientation (o), pensize(p) and size (s)
a=190
b=-350
o=90
s=8
l=s
p=s*.1
import turtle
turtle.speed(0)
turtle.pu()
turtle.pensize(p)
turtle.setposition(a,b)
turtle.setheading(o)
turtle.pd()

#draw top of head
turtle.circle(s*.6,45)
turtle.right(75)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*1.2,140)
p=s*.1

#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        turtle.fillcolor("grey")
        turtle.begin_fill()

        #start side edge
        turtle.right(75)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90) 
        turtle.circle(s*.6,70)
        turtle.left(125)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80) 
        turtle.fd(s*.3)
        turtle.right(40)
        turtle.circle(-s,110)

        #draw central spine
        turtle.left(140) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(-s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(s*.4,45)
        turtle.right(90)
        turtle.circle(s,110)
        
        turtle.left(45)
        turtle.fd(s*.6)
        turtle.left(70)

#draw tail section
#rear spine
turtle.begin_fill()
turtle.right(150)
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(-s*4,70)
p=s*.1
turtle.pensize(p)
#connecting tail 
turtle.right(120)
turtle.circle(s,90)
turtle.end_fill()

######################################left side now finished repeat on right, backwards
s=l
p=s*.1
turtle.pensize(p)
turtle.pu()
turtle.setposition(a,b)
turtle.setheading(o-180)
turtle.pd()

#draw top of head
turtle.circle(-s*.6,45)
turtle.right(75+180+30)

p=s*.5
#draw left side of head
for i in range(11):
        turtle.pensize(p)
        turtle.circle(-s,10)
        p=p-(p*.05)
p=s*.1 
turtle.right(90+180)

#draw left trilobite whisker
for i in range(7):
        turtle.pensize(p*2.5)
        turtle.circle(-s*1.2,20)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*1.2,140)
p=s*.1
#Draw body segments/legs on left
for s in [s,s*.9,s*.8,s*.7,s*.6]:
        #turtle.fillcolor("brown")
        turtle.begin_fill()
        #start side edge
        turtle.right(75+180+30)
        turtle.pensize(p)
        turtle.fd(s*.4)
        
        #draw leg
        turtle.right(90+180) 
        turtle.circle(-s*.6,70)
        turtle.left(125+110)
        turtle.fd(s*.6)
        turtle.end_fill()
        #draw inner segment
        turtle.begin_fill()
        turtle.left(80+200) 
        turtle.fd(s*.3)
        turtle.right(40+100+180)
        turtle.circle(s,110)
        
        #draw central spine
        turtle.left(140+80) 
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.fd(s*.9)
        turtle.left(180)
        turtle.right(140-100)
        turtle.end_fill()
        #draw inner circle half
        turtle.left(90)
        turtle.circle(s*.4,45)

        #return to edge
        turtle.right(180)
        turtle.circle(-s*.4,45)
        turtle.right(90+180)
        turtle.circle(-s,110)
        
        turtle.left(45+180+90)
        turtle.fd(s*.6)
        turtle.left(70+180+40)
#draw tail section
turtle.begin_fill()
turtle.right(150+60)
#rear spine
for i in range(7):
        turtle.pensize(p*3)
        turtle.circle(-s*4,10)
        p=p-(p*.1)
turtle.right(180)
turtle.pensize(1)
turtle.circle(s*4,70)
p=s*.1
#connecting tail
turtle.pensize(p)
turtle.right(120+120)
turtle.circle(-s,90)
turtle.end_fill()

#footprints
turtle.pu()
turtle.setposition(a,b)
turtle.left(105)
turtle.fd(s*8)
turtle.right(65)
turtle.fd(s*2)
for i in range (14):
        turtle.dot(s*.5)
        turtle.left(130)
        turtle.fd(s*4)
        turtle.dot(s*.5)
        turtle.right(125)
        turtle.fd(s*4)




###################write location
turtle.pu()
turtle.setposition(125,300)
turtle.write("A Look Back Into the", False, align="left", font=("TeXGyreSchola",30,"bold"))
turtle.setposition(125,250)
turtle.write("Paleozoic Era (542-251 Ma)", False, align="left", font=("TeXGyreSchola",30,"bold"))
turtle.hideturtle()
input()
