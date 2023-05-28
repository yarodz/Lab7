#Yanet Rodriguez
#May 28, 2023

#Problem 1-This problem returns the area of a circle

import math

def areaOfCircle(r):
    return math.pi * r * r

print(areaOfCircle(8))

#Problem 2-Check if number is in a given range

def checkrange(n):
    if n in range(1,10):
        print("Number it's in range")

    else:
        print("Number it's not in range")

n = int(input("Please Enter Number: "))
checkrange(n)

#Problem 3-Multiplies numbers on a list

def multiplylist(list):
    product = 1
    for i in list:
        product = product* i
    return product

list = [5,2,7,-1]
print ("Product is ", multiplylist(list))

#Problem 4-function to return unique elements

def newlist(list):
    uniquelist = []
    for i in list:
        if i not in uniquelist:
            uniquelist.append(i)
            
    return uniquelist

print (newlist([1, 3, 3, 3, 6, 2, 3, 5]))

#Problem 5
import turtle

def drawSquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

side = 20
width = 10
for squares in range(5):

    drawSquare(alex,side)
    alex.penup()
    alex.back(width)
    alex.right(90)
    alex.forward(width)
    alex.left(90)
    alex.pendown()
    side+=2*width
wn.exitonclick()

#Problem 6 Creates a s figure with polygons

import turtle

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("hotpink")
alex.speed(10)
alex.width(3)

number_of_sides = 6


for i in range (10):
        alex.left(36)
        for i in range(6):
                alex.forward(75)
                alex.left(360/number_of_sides)
                
alex.hideturtle()          
wn.exitonclick()
            
            




        
