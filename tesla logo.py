import turtle

turtle.Screen().bgcolor("black")

t = turtle.Turtle()
t.speed(20)
t.pensize(2)
t.penup()

t.setposition(-250,230)
t.pendown()
t.pencolor("red")
t.begin_fill()
t.color("red")
t.left(30)
for i in range(250):
 t.right(0.1)
 t.forward(1)
for i in range(300):
 t.right(0.1)
 t.forward(1)
t.right(90)
t.fd(40)
t.right(90)
for i in range(250):
 t.left(0.1)
 t.forward(1)
for i in range(265):
 t.left(0.12)
 t.forward(1)
t.right(90)
t.fd(35)
t.end_fill()

t.penup()
t.setposition(-220,180)
t.right(90)
t.pendown()
for i in range(220):
 t.right(0.12)
 t.forward(1)
t.right(60)
t.fd(70)
t.left(110)
t.fd(72)
t.right(65)
for i in range(185):
 t.right(0.08)
 t.forward(1)
t.right(85)
for i in range(70):
    t.right(0.55)
    t.fd(1)
t.right(110)
for i in range(35):
 t.left(1)
 t.fd(1)
for i in range(5):
 t.left(2)
 t.fd(1)
t.left(25)
t.fd(5)
t.fd(60)
#t.hideturtle()
turtle.done()


