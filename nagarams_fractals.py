#Antares Rahman & Katie Bixby
#Nov 22, 2013
#The program has two applications provided in a GUI. One checks for
#anagrams for a user-defined English word. The other creates fractals
#and allows the user to define some of the parameters.
##nagarams_fractals.py

from graphics import *
from buttonClass import *
from inputBoxClass import *
from displayInstructionsClass import *
from turtle import *
from fractalsClass import *
from checkAnagramsClass import checkAnagrams

def fractalOption(gwin):
    
    #####WINDOW 2 - FRACTALS WINDOW#####

    #Sidebar
    outline = Rectangle(Point(595,5), Point(997,597)) #Outline of the sidebar
    outline.draw(gwin)
    sideTitle = Text(Point(775, 25), "Fractals")
    sideTitle.setFace("courier")
    sideTitle.setSize(25)
    sideTitle.draw(gwin)
    #Iteration reccomendation
    ins = dispInstruct("iterationRecomm").file_read() #Text for the recommendation of iterations displayed in fractal window.
    instructions = Text(Point(730, 240), ins)
    instructions.setFace("courier")
    instructions.setSize(10)
    instructions.draw(gwin)

    #Buttons
    buttonLabel = Text(Point(925, 60), "Options:")
    buttonLabel.setFace("courier")
    buttonLabel.setSize(15)
    buttonLabel.draw(gwin) #Draws in "Options" label above buttons
    kCurveButton = Button(gwin, Point(925, 100), 100, 35, "Koch Curve") #Koch Curve button
    cCurveButton = Button(gwin, Point(925, 150), 100, 35, "C-Curve") #C-curve button
    gFractalButton = Button(gwin, Point(925, 200), 100, 35, "Gosper Island") #Gosper Island button
    cesFractalButton = Button(gwin, Point(925, 250), 100, 35, "Cesaro") #Cesaro button
    rTriangleButton = Button(gwin, Point(925, 300), 130, 35, "Repeat Triangles") #Repeat triangles button

    gridButton = Button(gwin, Point(910, 25), 45, 30, "Grid") #Button to create grid
    clearButton = Button(gwin, Point(965, 25), 45, 30, "Clear") #Clear button
    exitButton = Button(gwin, Point(630, 25), 38, 23, "Exit") #Exit button

    ##Creating the grid
    #Vertical lines
    xVal = 50 #start x value for first line
    for i in range(11): 
        lineV = Line(Point(xVal,0), Point(xVal, 600)) #Draws a vertical line
        lineV.setFill("pale turquoise")
        lineV.draw(gwin)
        xVal = xVal + 50 #Adds 50 to the x value for the next line, so it goes up by 50
    #Horizontal lines
    yVal = 50 #start y value for first line
    for i in range(11):
        lineH = Line(Point(0, yVal), Point(590, yVal)) #Draws a horizontal line
        lineH.setFill("pale turquoise")
        lineH.draw(gwin)
        yVal = yVal + 50 #Adds 50 to the next line, so it goes up by 50

    ##Input Boxes
    #Input Box 1 (Length of lines in drawing)
    inputBox1 = drawInputBox(gwin, 920, 410, 15, "Length of lines:").getInputBox()
    #Input Box 2 (# of iterations)
    inputBox2 = drawInputBox(gwin, 920, 460, 15, "Num of Iterations").getInputBox()
    #Input Box 3 (moveTo x-val)
    inputBox3 = drawInputBox(gwin, 920, 510, 15, "X-Val:").getInputBox()
    #Input Box 4 (moveTo y-val)
    inputBox4 = drawInputBox(gwin, 920, 560, 15, "Y-val:").getInputBox()
    #Input Box 5 (color)
    inputBox5 = drawInputBox(gwin, 920, 360, 15, "Color:").getInputBox()

    #Get user click
    pt = gwin.getMouse()
    
    while exitButton.clicked(pt) != True: #While the exit button hasn't been clicked
        #Get the input Results
        input1 = inputBox1.getText() #line length input
        if input1 == "":
            input1 = "50" #default if input1 blank
        input2 = inputBox2.getText() #iteration num input
        if input2 == "":
            input2 = "2" #default if input2 blank
        input3 = inputBox3.getText() #x-val input
        if input3 == "":
            input3 = "300" #default if input3 blank
        input4 = inputBox4.getText() #y-val input
        if input4 == "":
            input4 = "300" #default if input4 blank
        input5 = inputBox5.getText() #color input
        if input5 == "":
            input5 = "black" #default if input5 blank
        color = input5
        turtle = Turtle(gwin, color) #creating the turtle
        fractal = Fractal(gwin, turtle) #Creates instance of fractal class
        lt = eval(input1) #length
        n = eval(input2) #num iterations
        xVal = eval(input3) #start x-val
        origYVal = eval(input4) #inputted y-val
        #Altering y-val as per normal convention with the bottom left being (0,0) and the top right being (600,600)
        if origYVal < 300:
            difference = 300 - origYVal
            yVal = 300 + difference
        elif origYVal > 300:
            difference = origYVal - 300
            yVal = 300 - difference
        elif origYVal == 300:
            yVal = 300
        turtle.moveTo(Point(xVal,yVal)) #move turtle to starting point defined by user
        
        if kCurveButton.clicked(pt) == True: #If Koch curve button clicked
            fractal.kcurve(turtle, lt, n)
            turtle.turn(-2*pi/3)
            fractal.kcurve(turtle, lt, n)
            turtle.turn(-2*pi/3)
            fractal.kcurve(turtle, lt, n)
            turtle.turn(-2*pi/3) #returns the turtle's direction back to normal
            pt = gwin.getMouse() #get another mouse click

        elif cCurveButton.clicked(pt) == True: #If the user clicked the c-curve button
            turtle.turn(pi/2)
            fractal.cCurve(turtle, lt, n)
            turtle.turn(-pi/2) #returns the turtle's direction back to normal
            pt = gwin.getMouse() #get another mouse click

        elif gFractalButton.clicked(pt) == True: #If Gosper Island button clicked
            fractal.gFractal(turtle, lt, n)
            turtle.turn(-pi/3)
            fractal.gFractal(turtle, lt, n)
            turtle.turn(-pi/3)
            fractal.gFractal(turtle, lt, n)
            turtle.turn(-pi/3)
            fractal.gFractal(turtle, lt, n)
            turtle.turn(-pi/3)
            fractal.gFractal(turtle, lt, n)
            turtle.turn(-pi/3)
            fractal.gFractal(turtle, lt, n)
            turtle.turn(-pi/3) #returns the turtle's direction back to normal
            pt = gwin.getMouse() #get another mouse click

        elif cesFractalButton.clicked(pt) == True: #If Cesaro button clicked
            fractal.cFractal(turtle, lt, n)
            turtle.turn(-pi/2)
            fractal.cFractal(turtle, lt, n)
            turtle.turn(-pi/2)
            fractal.cFractal(turtle, lt, n)
            turtle.turn(-pi/2)
            fractal.cFractal(turtle, lt, n)
            turtle.turn(-pi/2) #returns the turtle's direction back to normal
            pt = gwin.getMouse() #get another mouse click
            
        elif rTriangleButton.clicked(pt) == True: #If repeating triangles button clicked
            turtle.turn(-pi/3)
            fractal.rTriangle(turtle, lt, n)
            turtle.turn(2*pi/3)
            fractal.rTriangle(turtle, lt, n)
            turtle.turn(2*pi/3)
            fractal.rTriangle(turtle, lt, n)
            turtle.turn(-pi/3) #returns the turtle's direction back to normal
            pt = gwin.getMouse() #get another mouse click

        elif clearButton.clicked(pt) == True:
            #Draws a plain white rectangle in place of the space where the fractals were being drawn
            whiteBG = Rectangle(Point(0,0), Point(593, 600))
            whiteBG.setFill("white")
            whiteBG.setOutline("white")
            whiteBG.draw(gwin)
            pt = gwin.getMouse() #get another mouse click

        elif gridButton.clicked(pt) == True:
            #Draws in the grid again
            #Vertical lines
            xVal = 50
            for i in range(11):
                lineV = Line(Point(xVal,0), Point(xVal, 600))
                lineV.setFill("pale turquoise")
                lineV.draw(gwin)
                xVal = xVal + 50
            #Horizontal lines
            yVal = 50
            for i in range(11):
                lineH = Line(Point(0, yVal), Point(590, yVal))
                lineH.setFill("pale turquoise")
                lineH.draw(gwin)
                yVal = yVal + 50
            pt = gwin.getMouse() #get another mouse click
        else: #If no button was clicked
            pt = gwin.getMouse() #get another mouse click

    gwin.close() #Closes the window when the while loop ends, which means the user clicked the exit button.
    

def anagramsOption(gwin):

    #####WINDOW 3 - ANAGRAMS WINDOW#####
    
    #Title
    title = Text(Point(300, 30), "Nagarams")
    title.setFace("courier")
    title.setSize(25)
    title.draw(gwin)
    #Description
    anaDescription = Text(Point(300, 135), "For this application, you simply have to input one\nEnglish word, and click anywhere (but the Exit button)\non the screen. The program will give you a list\nof all possible anagrams of the word.")
    anaDescription.setFace("courier")
    anaDescription.draw(gwin)

    #Exit button
    exitButton = Button(gwin, Point(550, 550), 30, 30, "Exit")
    
    #Ask input word from user
    inputBox = drawInputBox(gwin, 300, 260, 40, "Enter any English word of your choice:").getInputBox()

    #get user click
    pt = gwin.getMouse()    
    outputText = Text(Point(300, 375), "")
    outputText.setFace("courier")
    outputHead = Text(Point(300, 350), "")
    outputHead.setFace("courier")
    outputHead.draw(gwin)
    while exitButton.clicked(pt) != True:
        outputHead.setText("")
        #get the user inputted word
        word = inputBox.getText()
        #form an instance of the checkAnagrams(word) object, which is the lowercased string of the input word
        words = checkAnagrams(word)
        #list of all possible meaningful anagrams of the input word in lowercase. each word appears only once.
        outputWords = words.screenResults()
        i = 1
        y = 375
        outputTextList = []
        if len(outputWords) == 0: #If the user didn't input an English word
            outputText.setText("You did not enter an English word!")
            outputText.setFill("red4")
            outputText.draw(gwin)
        else: #If the user entered in an English word
            outputHead.setText("The following are anagrams of \'"+word.lower() + "\':")
            for w in outputWords: #loop through each word in the outputWords list
                anagramWord = str(i) + ". " + str(w) #draw in  each of the words
                outputText = Text(Point(300, y), anagramWord)
                outputText.setFace("courier")
                outputTextList.append(outputText)
                i += 1
                y = y+20 #If more than one anagram, makes each one appear 20px below the previous
            for i in range(len(outputTextList)):
                outputTextList[i].draw(gwin)
        pt = gwin.getMouse()
        outputText.setText("")
        outputText.undraw()
        for i in range(len(outputTextList)):
            outputTextList[i].undraw()
    gwin.close() #Closes the window when the while loop ends, which means the user clicked the exit button.
        
def main():
    
    ##### INTRO WINDOW #####
    win = GraphWin("Programming Assignment 6", 600,600)

    #Title and description
    title = Text(Point(300,75), "Fractals and Nagarams!")
    title.setFace("courier")
    title.setSize(20)
    title.draw(win)
    description = Text(Point(300, 240), "This program will allow you to perform two different\nfun activities! "\
                       "One that helps you draw "\
                       "fractals,\nand another that gives all the anagrams of "\
                       "an\nEnglish word."\
                       " To begin, simply click either the \'Fractals\'\nor the \'Anagrams\' button, and a pop out\nwindow will appear "\
                       "that runs the program of your choice.\nHave fun!")
    description.setFace("courier")
    description.setSize(11)
    description.draw(win)

    #Buttons for options
    option1Button = Button(win, Point(200,425), 100, 50, "Fractals")
    option2Button = Button(win, Point(400,425), 100, 50, "Nag a ram")
    #Exit button
    exitButton = Button(win, Point(550, 550), 30, 30, "Exit")
    
    #Get user click
    pt = win.getMouse()
    while exitButton.clicked(pt) != True:        
        #If the user selects the fractals option
        if option1Button.clicked(pt) == True:
            #Instructions
            dispInstruct("fractalsInstructions").GUIInstruct() #Text for popup instructions for Fractal program
            win2 = GraphWin("Fractals", 1000, 600) #creates a new window for the fractals option
            fractalOption(win2) #carries out the fractals option in the new window
            pt = win.getMouse()
            
        #If the user selects the anagrams option
        elif option2Button.clicked(pt) == True:
            win3 = GraphWin("Anagrams", 600, 600) #creates a new window for the anagrams option
            anagramsOption(win3) #carries out the anagrams option in the new window
            pt = win.getMouse()
            
        else:
            pt = win.getMouse()
            
    win.close()

main()
    
