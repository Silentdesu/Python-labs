from Person import *
'''Производный класс.'''

class Hombre(Person):

	def speak(self, msg):
		print(self.name, ':\tHola!', msg)