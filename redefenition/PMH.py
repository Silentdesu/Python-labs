from Man import *
from Hombre import *

osas = Man('Osas')
fuhrer = Hombre('Fuhrer')

osas.speak('it\'s a beautiful evening:\n')
fuhrer.speak('Es una tarde hermosa.\n')

Person.speak(osas)
Person.speak(fuhrer)