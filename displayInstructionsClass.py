#Antares Rahman
#Nov 22, 2013
#Class for displaying instructions

from graphics import *

class dispInstruct():
    """The class will read a .txt file given a filename
    then display the text on a separate window"""
    def __init__(self, filename):
        self.filename = filename
        
    ##File reader; reads the file named 'filename'.txt
    def file_read(self):
        """A file reader that reads the file the user enters in."""
        file = open(self.filename + ".txt", "r") #opens file named 'filename'.txt
        readFile = file.read() #reads the whole file as a string
        return readFile #returns one string containing the whole text

    ##reads the insWin.txt file on a separate window 'displayHelp'
    def GUIInstruct(self):
        """Reads the file entered in that contains the text the user wants to display and displays it on a separate window"""
        insWin = GraphWin("Instructions", 800, 680)
        insWin.setBackground("yellow")
        outputHelp = self.file_read()
        displayHelp = Text(Point(400,340),outputHelp)
        displayHelp.setFill("black")
        displayHelp.setStyle("bold")
        displayHelp.setSize(11)
        displayHelp.draw(insWin)
        #prompts click to close window
        closePrompt = Text(Point(400,670), "Click anywhere to close window and continue")
        closePrompt.setFill("black")
        closePrompt.draw(insWin)
        insWin.getMouse()
        insWin.close()
