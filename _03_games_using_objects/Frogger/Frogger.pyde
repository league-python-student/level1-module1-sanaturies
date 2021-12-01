
def setup():
    global frog_x, frog_y,bg,frog,kar
    frog_x=0
    frog_y=0
    bg = loadImage("froggerBackground.png")
    frog=loadImage('frog.png')
    kar=Car(frog_x,frog_y,100,100)
    # 1. Use the size function to set the size of your sketch
    size(1000,1000)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    frog.resize(50,50)
    bg.resize(1000,1000)
def draw():
    global frog_x, frog_y
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    image(frog,frog_x,frog_y)
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    kar.draw()
    kar.update()
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    if kar.x==frog_x and kar.y==frog_y :
        frog_x=0
        frog_y=0
    # 9. Create more car objects of different lengths, speed, and size
    a=Car(20,20,100,100)
    b=Car(60,30,200,19)
class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width