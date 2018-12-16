class Songbird():

	def __init__(self, name, song):
		self.name = name
		self.song = song
		print(self.name,'is born')

	def sing(self):
		print(self.name,'sings: ',self.song)

	def __del__(self):
		print(self.name,'flew away!\n')