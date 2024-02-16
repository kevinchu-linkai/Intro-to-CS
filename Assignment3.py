import random
ROW = 20
COL = 10
RESOLUTION_R = 400
RESOLUTION_C = 200
BLOCK_H = RESOLUTION_R/ROW
BLOCK_W = RESOLUTION_C/COL
block_exist = 0
point = 0
game_mode = 1
time = 0
class Blocks:
#init to set up attributes of the block class
  def __init__(self, a, b, c):
    self.row = a
    self.col = b
    self.color = c

#a method to display single block and its color
  def display(self):
    if self.color == 0:
      fill(255, 51, 52)
    elif self.color == 1:
      fill(12, 150, 228)
    elif self.color == 2:
      fill(30, 183, 66)
    elif self.color == 3:
      fill(246, 187, 0)
    elif self.color == 4:
      fill(76, 0, 153)
    elif self.color == 5:
      fill(255, 255, 255)
    elif self.color == 6:
      fill(0, 0, 0)
    elif self.color == 7:
      fill(210)
    rect(self.col*BLOCK_W,self.row*BLOCK_H,BLOCK_W,BLOCK_H)

class Tetris:
#init to set up attributes of the tetris class
  def __init__(self):
    global game_mode
    global time
    game_mode = 1
    time = 0
    self.speed = 0
    self.blocks = []
    for r in range(ROW):
      r_list=[]
      for c in range(COL):
        r_list.append(Blocks(r,c,7))
      self.blocks.append(r_list)

#a method to display all blocks in a tetris game
  def show(self):
    global point
    global block_exist 
    global block_now
    global game_mode
    if block_exist == 0:
      self.clean_point()
      block_exist = 1
      block_now = self.blockForm()
    else:
      block_now = self.drop(block_now)
      if block_now == 0:
           self.speed = self.speed + 0.25
           block_exist = 0
    for r in range(ROW):
        for c in range(COL):
            self.blocks[r][c].display()

#a method to get a specific block
  def getBlock(self, r, c):
    for i in range(ROW):
        for j in range(COL):
          if self.blocks[i][j].row == r and self.blocks[i][j].col == c:
               return self.blocks[i][j]
    return None

#a method to check if the down block of a block is empty
  def getDownEmpty(self, block):
    if block != 0 and self.getBlock(block.row+1,block.col) != None and self.getBlock(block.row+1,block.col).color == 7:
       return self.getBlock(block.row+1,block.col)
    return None

#a method to check if the right block of a block is empty
  def getRightEmpty(self, block):
    if block != 0 and self.getBlock(block.row,block.col+1) != None and self.getBlock(block.row,block.col+1).color == 7:
       return self.getBlock(block.row,block.col+1)
    return None

#a method to check if the left block of a block is empty
  def getLeftEmpty(self, block):
    if block != 0 and self.getBlock(block.row,block.col-1) != None and self.getBlock(block.row,block.col-1).color == 7:
       return self.getBlock(block.row,block.col-1)
    return None

#a method to swap two blocks
  def swap(self, block1, block2):
    tmp_color = block1.color
    block1.color = block2.color
    block2.color = tmp_color

#a method to form a random block at random column at the top row and check if the board is full
#if the board is full then stop the game 
  def blockForm(self):
    global time
    global game_mode
    global point
    n = 0
    r = 0
    c = random.randint(0,9)
    block = self.getBlock(r,c)
    while block.color != 7 and game_mode == 1:
      c = random.randint(0,9)
      if n == 30:
          break
      block = self.getBlock(r,c)
    if game_mode == 1:
        block.color = random.randint(0,6)
    for i in range(2):
        for j in range(COL):
            if self.blocks[i][j].color != 7:
                time += 1
                if time == 20:
                    game_mode = 0
            else:
                time = 0
                break
    return block

###a metod to swap the the colored block with an empty block under it
  def drop(self, block):
    empty = self.getDownEmpty(block)
    if empty != None:
        self.swap(block,empty)
        return empty
    else:
        return 0

##a metod to swap the the colored block with an empty block at its right
  def right(self, block):
    empty = self.getRightEmpty(block)
    if empty != None:
      self.swap(block,empty)
      block = empty
      return empty
    else:
      return block

#a metod to swap the the colored block with an empty block at its left
  def left(self, block):
    empty = self.getLeftEmpty(block)
    if empty != None:
        self.swap(block,empty)
        block = empty
        return empty
    else:
      return block
  
#a method to clear 4 vertical blocks in the same color and add a point
  def clean_point(self):
    global point
    global full
    for i in range(ROW-3):
      cnt = 0
      for j in range(COL):
        if self.blocks[i][j].color != 7:
          cnt = 1
          a = i +1
          while cnt != 0 and self.blocks[a][j].color == self.blocks[i][j].color:
            cnt = cnt +1
            a = a +1
            if cnt == 4:
                for k in range(cnt):
                    self.blocks[a-1-k][j].color = 7
                point = point +1
                self.speed = 0
                break
          cnt = 0

#create a Tetris object
tetris = Tetris()

#setup the game board
def setup():
  size(RESOLUTION_C,RESOLUTION_R)
  background(210)

#display the tetris and the texts
def draw():
  global game_mode
  global point
  #slow down the game by not calling the display() method every frame
  if frameCount%(max(1, int(8 - tetris.speed)))==0 or frameCount==1:
    background(210)
    tetris.show()
    for i in range(COL):
        line(i*BLOCK_W,0,i*BLOCK_W,RESOLUTION_R)
    for i in range(COL):
        line(0,i*BLOCK_H,RESOLUTION_C,i*BLOCK_H)
  fill(0,0,0)
  textSize(15)
  text('Point:'+str(point),10,30)
  if game_mode == 0:
    fill(0,0,0)
    textSize(30)
    text('GAME OVER',60,75,100,100)

#to control the blocks to go left or right
def keyPressed():
  global block_now
  if (key == CODED):
    if (keyCode == RIGHT):
      block_now = tetris.right(block_now)
    elif (keyCode == LEFT):
      block_now = tetris.left(block_now)

#restart the game by mouse click when game is over
def mouseClicked():
    global point
    if game_mode == 0:
        tetris.__init__()
        point = 0
  
  
     









