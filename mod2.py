import turtle

bob=turtle.Turtle()
bob.color("red","yellow")
bob.speed(20)


bob.begin_fill()
for i in range(10):
    bob.forward(300)
    bob.left(170)


bob.end_fill()