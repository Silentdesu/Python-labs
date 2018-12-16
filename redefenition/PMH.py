from Man import *
from Hombre import *

osas = Man('Osas') #Создаем экземпляр/переменную и присваиваем класс Man с атрибутом имени
fuhrer = Hombre('Fuhrer')

osas.speak('it\'s a beautiful evening:\n')#Вызываем у класса Man метод speak('обязательный текст')
fuhrer.speak('Es una tarde hermosa.\n')

Person.speak(osas)#Вызываем главный класс и его метод speak(готовый или можно создать новый экземпляр,msg(В нем уже есть по-дефолту сообщение,но можно и написать свое))
Person.speak(fuhrer)