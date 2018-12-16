from Person import *
'''Производный класс.'''

class Man(Person):

	def speak(self, msg):
		print(self.name,':\tHello!', msg)