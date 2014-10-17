#Christine Chung, Antares Rahman & Katie Bixby
#Nov 22, 2013
#Altered Turtle class

from graphics import *
from math import *

class Turtle:
    '''This Turtle class is used for drawing in a Zelle graphical window'''
    def __init__(self, win, color, x=0,y=0,direction=0): ###ADDED COLOR INPUT
        '''Constructor for turtle puts position at x,y and direction 0 radians'''
        self.win = win
        self.pt = Point(x,y)
        self.direction = 0.0  #0.0 points toward the positive direction of the x-axis
        self.color = color ###ADDED IN THE COLOR OF THE TURTLE

    def draw(self, length):
        '''Uses current direction and position and draws line of given length'''
        newPt = Point(self.pt.getX()+length*cos(self.direction), self.pt.getY()+length*sin(self.direction))
        line = Line(self.pt,newPt)
        line.setFill(self.color) ###ADDED IN FILLING IN THE COLOR OF THE LINES
        ###THE TURTLE DRAWS IN
        if self.pt.getX() < 590 and self.pt.getY() < 590: ###ADDED IN TO KEEP TURTLE FROM DRAWING INTO THE SIDE BAR IN THE
        ###PROGRAM
            line.draw(self.win)
        self.moveTo(newPt)

    def turn(self, rad):
        '''Turn the turtle by rad radians.
            Recall that radians are given in terms of pi = 180 degrees
            If rad is positive, turtle turns counterclockwise,
            If rad is negative, turtle turns clockwise.'''
        self.direction = self.direction+rad
        
    def moveTo(self, newPt):
        '''Set the turtle position to newPt, where newPt is a Point object'''
        self.pt = newPt

    def getPoint(self):
        x = self.pt.getX()
        y = self.pt.getY()
        return x,y

class Drawing:
    '''A class that has a graphical window with a quit button and a
        method to test if the quit button is clicked.'''
    def __init__(self, xcoord=100, ycoord=100):
        '''Constructor for Drawing class: creates a graphical window,
            set up coordinate range based on xcoord and ycoord params,
            and sets up a quit button'''
        self.win = GraphWin('Recursive Drawings', 500,500)
        #sets up coords so that (0,0) is toward bottom left of win
        self.win.setCoords(-xcoord/10.0, -ycoord/10.0, xcoord, ycoord)
        x = xcoord/10.0
        y = ycoord/10.0
        self.quitButton = Rectangle(Point(xcoord-x,-y), Point(xcoord,-y/2.0))
        self.quitButton.setFill("lightblue")
        self.quitButton.draw(self.win)
        Text(self.quitButton.getCenter(),"Quit").draw(self.win)

    def quit(self, pt):
        '''Assumes pt is the point where the user last clicked.
            Returns true if the pt is in the quit button.'''
        p1 = self.quitButton.getP1()
        p2 = self.quitButton.getP2()
        #if quit button was clicked
        if pt.getX() >= p1.getX() and pt.getX() <= p2.getX() and pt.getY() >= p1.getY() and pt.getY() <= p2.getY():
            return True
        else:
            return False


