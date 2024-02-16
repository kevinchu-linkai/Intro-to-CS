add_library('sound')
add_library('minim')
import random
import os
player = Minim(this)
class Game:
    def __init__(self, w, h, g, gr):
        self.speed = 0
        self.w = w
        self.h = h
        self.g = g
        self.gr = gr
        self.bgMusic = player.loadFile(os.getcwd() + "/data/background.mp3")
        self.level = 0
        self.kid = Player(self.g+100, self.g+100, self.g, 800, 100, 100)
        self.platforms = []
        self.spikerow = loadImage(os.getcwd() + "/data/" + "5.png")
        self.game_over = False
        self.cnt = 8
        self.bgMusic.loop()
        
    def form_platform(self):
        if self.cnt == 8:
            for i in range(8):
                position = random.randint(0,4)
                type = random.randint(0,4)
                self.cnt = self.cnt - 1
                self.platforms.append(Platform(120,25,position*120,(i+1)*100,type))
                
        for p in self.platforms:
            if p.y == 0:
                self.platforms.remove(p)
                self.level +=1
                self.cnt +=1
                break    
                        
        if self.game_over == False and self.cnt == 1:
            self.cnt = self.cnt - 1
            position = random.randint(0,4)
            type = random.randint(0,4)
            self.platforms.append(Platform(120,25,position*120,800,type))       
                
    def display(self):
        image(self.spikerow,0,0,120,51)
        image(self.spikerow,120,0,120,51)
        image(self.spikerow,240,0,120,51)
        image(self.spikerow,360,0,120,51)
        image(self.spikerow,480,0,120,51)
        
        for p in self.platforms:
            if self.game_over == False:
                p.move()
            p.display()
        self.kid.display()
        
class Player:
    def __init__(self, x, y, g, gr, char_w, char_h):
        self.x = x
        self.y = y
        self.g = g
        self.gr = gr
        self.char_w = char_w
        self.char_h = char_h
        self.vx = 0
        self.vy = 1
        self.on = 0
        self.life = 10
        self.dir = 1
        self.gameover_img = loadImage(os.getcwd() + "/data/end.png" )
        self.SpikeSound = SoundFile(this, os.getcwd() + "/data/spike.mp3")
        self.FireSound = SoundFile(this, os.getcwd() + "/data/fire.mp3")
        self.LandSound = SoundFile(this, os.getcwd() + "/data/land.mp3")
        self.ScreamSound = SoundFile(this, os.getcwd() + "/data/scream.mp3")
        self.keyHandler = {LEFT:False, RIGHT:False, UP: False}
        self.img1 = loadImage(os.getcwd() + "/data/" +'kid1.png')
        self.img2 = loadImage(os.getcwd() + "/data/" +'kid2.png')
    

    def gravity(self):
        if self.y + self.char_h < self.gr:
            self.vy += 0.5
        else:
            self.vy = 0
        for p in game.platforms:
            if p.x <= self.x+50 and self.x+50 <= p.x + p.w and self.y + self.char_h -p.y <= 30 and p.type != 4:
                self.gr = p.y
                return
        self.gr = game.gr

    def update(self):
        self.gravity()
        if self.keyHandler[LEFT]:
            self.vx = -7
            self.dir = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 7
            self.dir = 1
        else:
            self.vx = 0
             
        self.x += self.vx
        self.y += self.vy
        if self.y + self.char_h > self.gr:
            self.y = self.gr - self.char_h

        if self.vy == 0:
            for p in game.platforms:
                if self.on == 0 and p.x <= self.x + 50 and self.x + 50 <= p.x + p.w and self.y + self.char_h == p.y:
                    if p.type == 1:
                        self.SpikeSound.play()
                        self.reduce_life()
                        self.reduce_life()
                        self.on = 1
                    elif p.type == 2:
                        self.FireSound.play()
                        self.reduce_life()
                        self.on = 1
                    elif p.type == 0 or p.type == 3:
                        self.LandSound.play()
                        if self.life < 10:
                            self.plus_life()
                        self.on = 1
        else:
            self.on = 0

        if 800 - self.char_h == self.y and game.game_over == False:
            self.game_over()
        elif self.life <= 0 and game.game_over == False:
            self.game_over()
            
        if self.y + 50 <= 70:
            self.SpikeSound.play()
            self.y = 40
            self.reduce_life()
            
        if self.x < 1:
            self.x = 0
        elif self.x + self.char_w > 600:
            self.x = 600 - self.char_w 
        
    def reduce_life(self):
        self.life = self.life - 1
        
    def plus_life(self):
        self.life = self.life + 1
            
    def game_over(self):
        self.ScreamSound.play()
        game.game_over = True
    
    def display(self):
        self.update()
        if self.dir > 0:
            image(self.img1,self.x,self.y,self.char_w,self.char_h)
        if self.dir < 0:
            image(self.img2,self.x,self.y,self.char_w,self.char_h)

class Platform:
  def __init__(self,w,h,x,y,t):
    self.w = w
    self.h = h
    self.x = x
    self.y = y
    self.type = t
    self.img = loadImage(os.getcwd() + "/data/" + str(self.type)+ ".png")
    
  def move(self):
      self.y = self.y - 4 - (game.level/100)
  
  def display(self):
    image(self.img,self.x,self.y,self.w,self.h)

game = Game(600,800,51,800)
img = loadImage(os.getcwd() + "/data/" + "bg.jpeg")
def setup():
    size(game.w,game.h)

def draw():
    background(img)
    game.form_platform()
    game.display()
    fill(255,255,255)
    textSize(40)
    text('Score:'+str((game.level//50)+1),10,80)
    text('Life:'+str(game.kid.life),10,120)
    if game.game_over == True:
        image(game.kid.gameover_img,170,300,250,300)
    
def keyPressed():
    if keyCode == LEFT:
        game.kid.keyHandler[LEFT] = True 
    elif keyCode == RIGHT:
        game.kid.keyHandler[RIGHT] = True 

def keyReleased():
    if keyCode == LEFT:
        game.kid.keyHandler[LEFT] = False 
    elif keyCode == RIGHT:
        game.kid.keyHandler[RIGHT] = False 
        
def mouseClicked():
    global game
    if game.game_over == True:
        game = Game(600,800,51,800)
