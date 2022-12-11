import turtle
turtle.setup(600, 600)
turtle.bgcolor("black")

turtle.color("white")
turtle.speed(0)
turtle.width(6)

for i in range(110):
    turtle.forward(i*5)
    turtle.right(90)

turtle.Screen().exitonclick()