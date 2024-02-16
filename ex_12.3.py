class bank:
	def __init__(self, a, b, c):
		self.__balance = a
		self.__name = b
		self.__account_number = c

	def deposit(self, amount):
		self.__balance = self.__balance + amount

	def withdraw(self, amount):
		self.__balance = self.__balance - amount

	def get_balance(self):
		return self.__balance

	def print_balance(self):
		print(self.__balance)

bank1 = bank(3,'kevin','0206')
bank1.print_balance()
bank1.deposit(2)
bank1.print_balance()
bank1.withdraw(2)
print(bank1.get_balance())