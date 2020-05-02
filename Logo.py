import turtle
from turtle import Turtle
import math
import random
from random import randint
from turtle import *

def ground_bgcolor(c):
    showturtle()
    penup()
    w = 1000
    h = 1000
    penwidth = 10
    # set a big pen width so the turtle is visible while drawing
    width(penwidth)
    # adjust position so we're inside the window border
    goto(-w/2 + penwidth/2, -h/2+penwidth)
    setheading(90)  # north

    pendown()
    color(c, c)     # set both drawing and fill color to be the same color
    begin_fill()
    forward(h/2 - penwidth)
    right(90)
    forward(w - penwidth)
    right(90)
    forward(h/2 - penwidth)   # could be optimized..
    right(90)
    forward(w - penwidth)
    right(90)
    end_fill()

    penup()
    goto(0,0)  # end by setting the turtle in the middle of the screen
    width(1)
    color('black', 'white')
    setheading(90)

screen = Screen()
ground_bgcolor('green')

screen = Screen()
def tree(branchLen,t):
    if branchLen > 3:
        t.forward(branchLen)
        t.right(15)
        tree(branchLen-8,t)
        t.left(30)
        tree(branchLen-8,t)
        t.right(15)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    t.speed(0)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("gold")
    tree(75,t)
    myWin.exitonclick()
screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Random Cloud - PythonTurtle.Academy")

turtle.speed(0)
turtle.hideturtle()
turtle.up()
turtle.bgcolor('dodger blue')
turtle.pencolor('white')
turtle.pensize(2)

n = 500 # number of points on each ellipse
# X,Y is the center of ellipse, a is radius on x-axis, b is radius on y-axis
# ts is the starting angle of the ellipse, te is the ending angle of the ellipse
# P is the list of coordinates of the points on the ellipse
def ellipse(X,Y,a,b,ts,te,P):
    t = ts
    for i in range(n):
        x = a*math.cos(t)
        y = b*math.sin(t)
        P.append((x+X,y+Y))
        t += (te-ts)/(n-1)

# computes Euclidean distance between p1 and p2
def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

# draws an arc from p1 to p2 with extent value ext
def draw_arc(p1,p2,ext):
    turtle.up()
    turtle.goto(p1)
    turtle.seth(turtle.towards(p2))
    a = turtle.heading()
    b = 360-ext
    c = (180-b)/2
    d = a-c
    e = d-90
    r = dist(p1,p2)/2/math.sin(math.radians(b/2)) # r is the radius of the arc
    turtle.seth(e) # e is initial heading of the circle
    turtle.down()
    turtle.circle(r,ext,100)
    return (turtle.xcor(),turtle.ycor()) # returns the landing position of the circle
                                         # this position should be extremely close to p2 but may not be exactly the same
                                         # return this for continuous drawing to the next point


def cloud(P):
    step = n//10 # draw about 10 arcs on top and bottom part of cloud
    a = 0 # a is index of first point
    b = a + random.randint(step//2,step*2) # b is index of second point
    p1 = P[a] # p1 is the position of the first point
    p2 = P[b] # p2 is the position of the second point
    turtle.fillcolor('white')
    turtle.begin_fill()
    p3 = draw_arc(p1,p2,random.uniform(70,180)) # draws the arc with random extention
    while b < len(P)-1:
        p1 = p3 # start from the end of the last arc
        if b < len(P)/2: # first half is top, more ragged
            ext = random.uniform(70,180)
            b += random.randint(step//2,step*2)
        else: # second half is bottom, more smooth
            ext = random.uniform(30,70)
            b += random.randint(step,step*2)
        b = min(b,len(P)-1) # make sure to not skip past the last point
        p2 = P[b] # second point
        p3 = draw_arc(p1,p2,ext) # draws an arc and return the end position
    turtle.end_fill()
MAX_SLOPE = 45
MIN_SLOPE = -45
MIN_HEIGHT = 0
def dist_squared(P1,P2):
    return (P1[0]-P2[0])**2 + (P1[1]-P2[1])**2

def mountain(P1,P2):
    if dist_squared(P1,P2) < 9:
        turtle.goto(P2)
        return
    turtle.color('black')
    x1,y1 = P1
    x2,y2 = P2
    x3 = random.uniform(x1,x2)
    y3_max = min((x3-x1)*math.tan(math.radians(MAX_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MIN_SLOPE)) + y2)
    y3_min = max((x3-x1)*math.tan(math.radians(MIN_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MAX_SLOPE)) + y2)
    y3_min = max(y3_min, MIN_HEIGHT)
    y3 = random.uniform(y3_min,y3_max)
    P3 = (x3, y3)
    mountain(P1,P3)
    mountain(P3,P2)
    return
turtle.speed(0)
turtle.up()
turtle.goto(-400,MIN_HEIGHT)
turtle.down()
mountain((-400,MIN_HEIGHT),(400,MIN_HEIGHT))
P = [] # starting from empty list
ellipse(200,200,200,100,0,math.pi,P) # taller top half
ellipse(200,200,200,25,math.pi,math.pi*2,P) # shorter bottom half
cloud(P)
G = []
ellipse(-200,200,200,100,0,math.pi,G) # taller top half
ellipse(-200,200,200,25,math.pi,math.pi*2,G) # shorter bottom half
cloud(G)
main()
grass = Turtle()
grass.color('#007b0c')

tuft = Turtle()

cut = Turtle()
cut.speed(0)
    

lake = Turtle()


turtles = [grass,lake,tuft]

def penup():
    for i in turtles:
        i.penup()
def pendown():
    for i in turtles:
        i.pendown()
def speed():
    for i in turtles:
        i.speed(0)
        i.hideturtle()


hexnum = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

penup()
pendown()

browns = ['#7a5230','#614126','#49311c','#302013','#181009']
greens = ['#004000','#003300','#002600','#001900','#004c00']


def drawgrass(amount,locx,locy):
    tuft.color('#004000')
    tuft.hideturtle()
    def tuftdraw(size):
        if randint(0,1) == 1:
            size = -size
        tuft.color(greens[randint(0,4)]) 
        penup()
        tuft.goto(locx+size,locy+size)
        pendown()
        tuft.goto(locx+5+size,locy+10+size)
        tuft.goto(locx+size,locy+size)
        tuft.goto(locx-5+size,locy+10+size)
        tuft.goto(locx-1+size,locy-1+size)
        tuft.goto(locx+3+size,locy+6+size)
        tuft.goto(locx+1+size,locy-1+size)
        tuft.goto(locx-2+size,locy+5+size)
    for i in range(amount):
        for i in range(randint(1,4)):
            tuftdraw(i*3)

    def grassdraw():
        penup()
        grass.goto(randint(-160,-150),randint(-240,-190))
        
        pendown()
        grass.begin_fill()
        for i in range(200):
            grass.color(greens[randint(0,4)])
            grass.goto(randint(-300,-50),randint(-200,-150))
        
        grass.end_fill()

def lakedraw():
    print("\nDrawing lake")
    blues = ['00004c','000066','000099','0000b2','0000cc','0000e5','0000ff']

    penup()
    lake.goto(randint(-50,50),randint(-170,-150))
    temp = Turtle()
    temp.penup()
    temp.hideturtle()
    temp.goto(lake.pos())
    pendown()

    lake.begin_fill()

    lake.pensize(5)
    for i in range(50):
        lake.color("#"+blues[randint(0,6)])
        lake.forward(5)
        lake.right(randint(0,5)/10)
        if randint(0,2) == 2:
            drawgrass(5,lake.pos()[0],lake.pos()[1])
    while lake.heading() > 185:
        lake.color("#"+blues[randint(0,6)])
        lake.forward(2)
        lake.right(randint(-2,8))
    for i in range(50):
        lake.color("#"+blues[randint(0,6)])
        lake.forward(5)
        lake.left(randint(0,2)/10)
    for i in range(100):
        lake.color("#"+blues[randint(0,6)])
        lake.forward(5)
        lake.right(randint(0,8)/10)
        
    lake.color("#"+blues[1])
    lake.goto(temp.pos())
    lake.end_fill()





speed() 


lakedraw()
