from datetime import *

today = datetime.today()#Делаем объявление переменной и присваиваем ей сегодняшний год\месяц\число\часы\минуты\секунды\микросекунды
print("Today is: ",today)
for attr in ['year','month','day','hour','minute','second','microsecond']:#Каждый раз отдельно посмотреть тоже самое,но выведет в списке
	print(attr,':\t',getattr(today,attr))
print("Time: ",today.hour,":",today.minute,sep='')#Выведит время к которому мы привыкли,т.е. час\минута
day = today.strftime('%A')#Форматирует так,чтобы показать день недели,если заглавная А,то выводит полностью название,если маленькую а,то выведит сокращенно
month = today.strftime('%B')#Так же выводит название месяца,а маленькая b сокращенный вид
print("Date: ",day,month,today.day)
'''Just for me,I made this to look how it's working'''