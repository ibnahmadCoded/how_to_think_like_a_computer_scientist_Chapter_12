import turtle
import time

def show_poly():
    try:
        win = turtle.Screen()       #Grab/Create a resource, e.g. a window
        tess = turtle.Turtle()


        #This dialog could be cancelled
        #or the conversion to int might fail, or might be zero.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360/n
        for i in range(n):      #Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)           #Make the program wait a few seconds
    finally:
        win.bye()               #Close the turtle's window


show_poly()
show_poly()
show_poly()
