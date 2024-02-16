add_library('sound')
add_library('minim')
import os
import random

class game:
	def __init__(self,w,h,g):
		self.w = w
		self.h = h
		self.g = g
		self.kid
		self.bg
		self.bgmusic
		self.pause
		self.platforms
		self.floors

	def form_platform(self):

	def touch_platform(self):

	def display(self):

class Platform:
	def __init__(self,w,h,x,y,t,img):
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.type = t
		self.img = loadImage(os.getcwd() + "/data/" + "t" + img)

    def display(self):
        image(self.img, self.x, self.y)

game = Game(1280, 720, 585)

def setup():
    size(game.w, game.h)
    
def draw():
    if game.pause == False:
        background(255, 255, 255)
        game.display()
    
def keyPressed():
    if key == 'p' and game.pause == False:
        game.pause = True
        game.bgMusic.pause()
    elif key == 'p' and game.pause == True:
        game.pause = False
        game.bgMusic.play()
        
        
    if keyCode == LEFT:
        game.mario.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        game.mario.keyHandler[RIGHT] = True
    elif keyCode == UP:
        game.mario.keyHandler[UP] = True
        
def keyReleased():
    if keyCode == LEFT:
        game.mario.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.mario.keyHandler[RIGHT] = False
    elif keyCode == UP:
        game.mario.keyHandler[UP] = False
        