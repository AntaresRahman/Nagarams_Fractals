#Katie Bixby
#Nov 22, 2013
#Class for creating inputbox 

from graphics import *

class drawInputBox:
    """in the GraphWin object gwin, this function creates a yellow Entry object
    centred at the Point(ptX, ptY) with a limit of lim characters"""
    def __init__(self, gwin, ptX, ptY, lim, label):
        self.inputBox = Entry(Point(ptX,ptY),lim) #Creates input box
        self.inputBox.setFill("yellow") #Colors the input box yellow
        inputBoxTitle = Text(Point(ptX, ptY-20), label) #creates title for input box
        self.inputBox.draw(gwin) #Draws input box
        inputBoxTitle.draw(gwin) #Draws in title for input box
    def getInputBox(self):
        """Returns the content of the input box"""
        return self.inputBox
