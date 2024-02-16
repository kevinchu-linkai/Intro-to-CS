class Employee:
	def __init__(self, name, number):
		self.__name = name
		self.__number = number

	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

class Produycion_Worker(Employee):
	def __init__(self, name, number, shift_num, pay):
		super().__init__(name, number)
		self.__shift_num = shift_num
		self.__pay_rate = pay
		
	def get_shift_num(self):
		return self.__shift_num

	def set_shift_num(self,x):
		self.__shift_num = x

	def get_pay(self):
		return self.__pay_rate

	def set_pay(self, x):
		self.__pay_rate = x

