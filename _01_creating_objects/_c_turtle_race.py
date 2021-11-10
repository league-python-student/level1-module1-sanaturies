"""
Turtle Race
"""
import turtle
import random
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'C:\\Users\\sanam\\Programming\\Pyflakes\\level1-module1-sanaturies\\_01_creating_objects\\race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return
    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)
    return image.width,image.height
# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    draw_background()
    t=turtle.Turtle()
    # TODO 1) Create an empty list of turtles
    dictionary={
            'a':'',
            'b':'',
            'c':'',
            'd':'',
            'e':'',
            'f':'',
            'g':'',
            'h':''
        }
    # TODO 2) Create a new turtle and set its shape to 'turtle
    x1=-437
    y1=-272
    x2=435
    lst=['a','b','c','d','e','f','g','h']
    lsty=[]
    lstx=[]
    for i in range(len(lst)):
        dictionary[lst[i]]=turtle.Turtle()
    # TODO 3) Set the turtle's speed to 3
        dictionary[lst[i]].speed(3)
    # TODO 4) Set the turtle's pen up
        dictionary[lst[i]].penup()
    # TODO 5) Use the turtle's goto() method to set its position on the left
    #  side of the screen
        y1+=54.5
        dictionary[lst[i]].goto(x1+40,y1+20)
        lsty.append(y1)
        lstx.append(x1)
    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  ** click on the window to print the corresponding x, y location

    
    # TODO 7) Move each turtle forward a random distance between 1 and 20
    while lstx[i]<x2-40: 
        for i in range(len(lst)):
            rand=random.randint(1,20)
            lstx[i]+=rand
            dictionary[lst[i]].goto(lstx[i],lsty[i])
            if lstx[i]>x2-40:
                break
            
            
    print(lst[i])
    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish line
    #  *HINT* click on the window to print the corresponding x, y location

    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race.

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!

    turtle.done()
