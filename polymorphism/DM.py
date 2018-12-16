from Duck import *
from Mouse import *

def describe(object): #Создаем функцию и вызываем из классов методы,если они действительно есть в классе,то он вызовутся,а если нет,то выдаст ошибку
	object.talk()
	object.coat()

donald = Duck()
mickey = Mouse()

describe(donald)
describe(mickey)