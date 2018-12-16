from Bird import *

print('Class Instances Of: ',Bird.__doc__)#Выводит документацию в классе Bird
polly = Bird('Tweet, tweet')#Создаем экземпляр/переменную присваивающую класс Bird и даем аргумент в конструктор init Tweet,tweet
print('Number Of Birds: ',polly.count)#Выводит атрибут count в переменной по-умолчанию = 0 и после создания экземпляров присваивает +=1
print('Polly Says: ',polly.talk())#В классе Bird есть метод talk,который возвращает значение аргументы из конструктора init Tweet,tweet
polly.age = '1 weeks' #Создаем новый атрибут age в экземпляр и в класс Bird
print('Polly\'s age: ',polly.age)
donald = Bird('Quack,quack')#Создаем вторую экземпляр/переменную и атрибут count снова присваивает +=1
donald.age = '100 weeks'#Также создаем в экземпляре/переменной Donald атрибут age
print('Number Of Birds: ',donald.count)#Count = 2
print('Donald Says: ',donald.talk())
print('Donald\'s Age: ',donald.age)
print('\n\n\n\n')
setattr(polly,'age','101 weeks')#тоже самое,что и на линии 7 и 10,только тут специальная встроенная функция в Python(присваивание и создание нового атрибута)
print('Polly\'s Age After 100 Weeks: ',polly.age)
print('\nPolly\'s Attributes...')
delattr(polly,'age')#При помощи встроенной функции удаляем из экземпляра/переменной Polly атрибут age
for attrib in dir(polly):#Создаем цикл и при помощи функции dir() смотрим в экземпляре/переменной Polly все доступные атрибуты 
	if attrib[0] != "_":#Если первый знак не равен _,а это именно такие атрибуты как __doc__,вывести атрибуты без _
			print(attrib,getattr(polly,attrib),sep=":")
for attrib in dir(donald):
	if attrib[0] != '_':
		print(attrib,getattr(donald,attrib),sep=":")
print('\nDonald\'s Age Attribute?',hasattr(donald,'talk'))#Встроенная функция hasattr(экземпляр,'атрибут') проверяем существуеи ли экземпляре этот атрибут,если да(True),нет(False)