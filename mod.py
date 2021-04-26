import turtle


bob = turtle.Turtle()

bob.color("blue","red")

bob.begin_fill()

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
# bob.end_fill()    
# space
bob.penup()
bob.forward(150)
bob.pendown()
# second square
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

bob.end_fill()




turtle.done()