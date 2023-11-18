from turtle import *
import time

color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

hideturtle()
speed(0) # Maximum speed
delay(0) # No delay
tracer(0) # Turn off screen updates

# Wait for 10 seconds
for _ in range(50):
    update()
    time.sleep(0.1)

# Turn on screen updates and show the turtle
tracer(1)
done()