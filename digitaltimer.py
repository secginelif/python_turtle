seconds=57
minutes=44

import turtle
import time

bob=turtle.Turtle()
bob.hideturtle()
bob.screen.bgcolor("grey")
bob.color("white")
bob.screen.setup (width=500, height=500, startx=0, starty=0)


while True:
    bob.clear()
    bob.write(str(minutes).zfill(2)+":"+str(seconds).zfill(2),font=("arial",30))
    seconds = seconds+1
    time.sleep(1)
    if seconds== 60:
        seconds = 0
        minutes= minutes+ 1
    elif minutes==45:
        bob.clear()
        time.sleep(0.1)
        bob.write("done",font=("arial",30))
        break

bob.bye()

turtle.done()