Nagarams & Fractals
=================
by Antares Rahman, Katie Bixby

Python Programming Project

Instructor: Christine Chung

November 22, 2013


Run nagarams_fractals.py

Nagarams: The name comes from the Google Search easter egg where searching for "anagram" suggests "Did you mean: nag a ram". This part of the program essentially takes a user-defined English word, binary searches through a dictionary of English words, and prints out all possible English anagrams of that word.

The program might take time if a large word is used.


Fractals: This part of the program takes various user-defined parameters to produce different fractal diagrams.

You have many options for customizing various fractals here (or recursive drawings, as seen in the case of the repeat triangles option). These options include changing the Colors, Lengths of the Lines, Number of Iterations, and x and y Values of the Original Starting point of any fractal you want drawn. You can draw as many fractals as you want!

I have laid out a grid to help you plot your fractals. With each line, the x and y values go up by 50px, starting with (0,0) as the bottom left, and ending with (600,600) as the top right. So if you wanted to draw a fractal at the point where the first vertical and horizontal lines from the bottom left cross, you would enter 50 as your x-value, and 50 as your y-value. If you don't want a grid, however, just click 'Clear'!

You can also click 'Clear' at any time to clear off any fractals you've already drawn in.  However, since this also clears away the grid, if you want to draw the grid back in, simply click the 'Grid' button next to 'Clear', and it will be drawn back in!
If you leave any of the customization options blank, the program will use the default options that have been set in order to draw in any fractals.

Also, here are the recommended iteration values for you to use on each fractal:
    
    Koch Curve: 1-4
    
    C-Curve: 8-10
    
    Gosper Island Fractal: 1-4
    
    Cesaro Fractal: 1-4
    
    Repeating Triangles: 1-3

Please avoid going over the iteration limit by too much. The program might crash if you do.

