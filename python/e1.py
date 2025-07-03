import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("#1a1a40")
screen.title("Sussy Crewmate")

t = turtle.Turtle()
t.speed(0)
t.pensize(8)
t.color("black")

# Starting position
t.penup()
t.goto(-50, -50)
t.setheading(0)
t.pendown()

# Body
t.fillcolor("red")
t.begin_fill()
t.forward(50)
t.circle(20, 90)
t.forward(100)
t.circle(20, 90)
t.forward(50)
t.circle(20, 90)
t.forward(100)
t.circle(20, 90)
t.end_fill()

# Backpack
t.penup()
t.goto(-80, -30)
t.setheading(90)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.end_fill()

# Visor
t.penup()
t.goto(-15, 10)
t.setheading(0)
t.pendown()

t.fillcolor("#93e9f7")
t.begin_fill()
t.forward(30)
t.circle(15, 180)
t.forward(30)
t.circle(15, 180)
t.end_fill()

t.hideturtle()
turtle.done()
