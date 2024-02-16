import random
class coin:
	def __init__(self, side=0):
		self.side_up = side

	def toss(self):
		self.side_up = random.randint(0,1)
		