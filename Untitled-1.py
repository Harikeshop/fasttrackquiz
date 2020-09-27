from turtle import * 
import turtle 

color = ['red' , 'green' , 'violet' , 'black']

def Shapes(size , sides):
    for x in range(sides):
        forward(size)
        left(360/sides)
        

for x in range(100):
    circle(5*x, x)
    left(x)
    speed('fast')
    
