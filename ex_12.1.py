class Tally_counter:
	def __init__(self, color='white'):
		self.counter = 0
		self.max_value = 9999
		self.color = color

	def click(self):
		if self.counter < self.max_value:
			self.counter += 1
		else:
			self.counter = 0

	def reset(self):
		self.counter = 0

tally1 = Tally_counter('red')
tally1.click()
tally1.click()
print(tally1.counter)
tally1.reset()
print(tally1.counter)
