#TurtleGraphics.py
#Name: Ella Falk
#Date: 2/12/25
#Assignment: Lab 4

import turtle

# Hides the default turtle in CodeHS
hideturtle()

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawSquareConcentric(myTurtle, size):
    myTurtle.penup()
    myTurtle.goto(-size / 100000, size / 2)  
    myTurtle.pendown()
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360 / sides)

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



def squaresInSquares(tom, numberSquares, size=100):
    step = size / numberSquares  # Size decrease per step
    
    for i in range(numberSquares):
        current_size = size - (i * step)
        drawSquareConcentric(tom, current_size)

def main():
    myTurtle = turtle.Turtle()

    # Draw a pentagon
    myTurtle.penup()
    myTurtle.goto(-150, 150)
    myTurtle.pendown()
    drawPolygon(myTurtle, 5)

    # Draw an octagon
    myTurtle.penup()
    myTurtle.goto(-150, 50)
    myTurtle.pendown()
    drawPolygon(myTurtle, 8)

    # Draw square with top right corner filled
    myTurtle.penup()
    myTurtle.goto(-10, 190)
    myTurtle.pendown()
    fillCorner(myTurtle, 2)

    # Draw square with bottom left corner filled
    myTurtle.penup()
    myTurtle.goto(-10, 50)
    myTurtle.pendown()
    fillCorner(myTurtle, 3)

    # Draw concentric squares with 5 squares
    myTurtle.penup()
    myTurtle.goto(0, 0)  # Center the squares
    myTurtle.pendown()
    squaresInSquares(myTurtle, 5)  # Draws 5 concentric squares

    # Reset position and draw 3 concentric squares in a new location
    myTurtle.penup()
    myTurtle.goto(200, 0)  # Move to a new position
    myTurtle.pendown()
    squaresInSquares(myTurtle, 3)  # Draws 3 concentric squares


main()