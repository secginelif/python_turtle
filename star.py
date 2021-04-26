import turtle

pegasus= turtle.Turtle()

pegasus.getscreen().bgcolor("pink")

def star(turtle,size):
    for i in range(5):
        turtle.forward(size)
        turtle.left(216)

star(pegasus,100)



turtle.done()