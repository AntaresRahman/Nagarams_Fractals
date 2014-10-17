#Katie Bixby
#Nov 22, 2013
#Class for drawing fractals

from graphics import *
from math import *
from turtle import *

class Fractal:
    """This Fractal class is used for drawing fractals in a Zelle graphical window using the Turtle Class"""
    def __init__(self, gwin, turtle):
        self.win = gwin
        self.turtle = turtle
            
    def kcurve(self, turtle, length, level):
        """Draws a Koch curve of given recursion level"""
        if level == 0:    #base case
            #draws a line in the current direction "length" long
            self.turtle.draw(length)
        else:
            length1 = length/3
            level1 = level-1
            self.kcurve(turtle, length1, level1)
            self.turtle.turn(pi/3)
            self.kcurve(turtle, length1, level1)
            self.turtle.turn(-2*pi/3)
            self.kcurve(turtle, length1, level1)
            self.turtle.turn(pi/3)
            self.kcurve(turtle, length1, level1)

    def cCurve(self, turtle, length, level):
        """Draws a c-curve of given recursion level"""
        if level == 0: #base case
            #draws a line in the current direction "length" long
            self.turtle.draw(length)
        else:
            level1 = level-1
            self.turtle.turn(pi/4)
            self.cCurve(self.turtle, length/sqrt(2), level1)
            self.turtle.turn(-pi/2)
            self.cCurve(self.turtle, length/sqrt(2), level1)
            self.turtle.turn(pi/4)
            
    def gFractal(self, turtle, length, level):
        """Draws a Gosper Island fractal of given recursion level"""
        if level == 0: #base case
            #draws a line in the current direction "length" long
            self.turtle.draw(length)
        else:
            length1 = length/3
            level1 = level-1
            self.gFractal(turtle, length1, level1)
            self.turtle.turn(pi/3)
            self.gFractal(turtle, length1, level1)
            self.turtle.turn(-pi/3)
            self.gFractal(turtle, length1, level1)
            
    def cFractal(self, turtle, length, level):
        """Draws a Cesaro Fractal of given recursion level"""
        if level == 0:    #base case
            #draws a line in the current direction "length" long 
            self.turtle.draw(length)
        else:
            length1 = length/3
            level1 = level-1
            self.cFractal(turtle, length1, level1)
            self.turtle.turn(-2*pi/5)
            self.cFractal(turtle, length1, level1)
            self.turtle.turn(4*pi/5)
            self.cFractal(turtle, length1, level1)
            self.turtle.turn(-2*pi/5)
            self.cFractal(turtle, length1, level1)

    def rTriangle(self, turtle, length, level):
        """Draws repeating triangles of given recursion level"""
        
        if level == 0: #base case
            #draws a line in the current direction "length" long
            self.turtle.draw(length)
        else:
            length1 = length/2
            level1 = level-1
            self.rTriangle(turtle, length1, level1)
            self.turtle.turn(2*pi/3)
            self.rTriangle(turtle, length1, level1)
            self.turtle.turn(-pi)
            self.rTriangle(turtle, length1, level1)
            self.turtle.turn(2*pi/3)
            self.rTriangle(turtle, length1, level1)
            self.turtle.turn(-pi)
            self.rTriangle(turtle, length1, level1)
            self.turtle.turn(2*pi/3)
            self.rTriangle(turtle, length1, level1)
