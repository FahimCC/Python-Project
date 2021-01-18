from turtle import *

def func(angle):
    begin_fill()
    left(angle)
    forward(200)
    circle(80, 180)
    left(260)
    circle(80, 180)
    forward(200)
    end_fill()



color("red")
func(50)
func(-20)
func(-20)
done()
