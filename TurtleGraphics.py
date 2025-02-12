#TurtleGraphics.py
#Name: Ella Falk
#Date: 2/12/25
#Assignment: Lab 4

import turtle
hideturtle() #hides the default turtle in CodeHS


def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.forward(100)
        alice.right(90)
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        

def drawSquareConcentric(tom, size):
    tom.penup()
    tom.goto(-size / 2, size / 2)  # Move to top-left corner
    tom.pendown()
    for i in range(4):
        tom.forward(size)
        tom.right(90)

def squaresInSquares(hole, numberSquares, size=100):
    step = size / numberSquares  # Decrease in size for each inner square
    for i in range(numberSquares):
        current_size = size - (i * step)
        drawSquareConcentric(hole, current_size)
        
def main():
    myTurtle = turtle.Turtle()
    
    myTurtle.up()
    myTurtle.goto(-150, 150)
    myTurtle.down()
    
    drawPolygon(myTurtle, 5) #draws a pentagon
    
    myTurtle.up()
    myTurtle.goto(-150, 50)
    myTurtle.down()
    
    drawPolygon(myTurtle, 8) #draws an octogon
    
    myTurtle.up()
    myTurtle.goto(-10, 190)
    myTurtle.down()
    

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    
    myTurtle.up()
    myTurtle.goto(-10, 50)
    myTurtle.down()
    
    fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    
    myTurtle.up()
    myTurtle.goto(-170, -100)
    myTurtle.down()

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()