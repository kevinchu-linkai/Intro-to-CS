import math
class point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '({},{})'.format(self.x,self.y)
	def distance(self):
		return (self.x**2+self.y**2)**0.5

class rectangle:
	def __init__(self, point, w, h):
		self.origin = point
		self.w = w
		self.h = h

	def __str__(self):
		return "({0},{1},{2})".format(self.origin, self.w, self.h)

	def resize(self, w, h):
		self.w = w
		self.h = h

	def replace(self, x, y):
		self.origin = point(x, y)

t1 = rectangle(point(1,2),3,4)
print(t1)
t1.resize(12,13)
print(t1)
t1.replace(-10,10)
print(t1)