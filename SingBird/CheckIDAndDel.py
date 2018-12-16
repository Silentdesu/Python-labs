from Songbird import *

donald = Songbird('Donald Duck','Quack-quack!')#Создаем экземпляр/переменную и присваиваем 2 атрибута('имя', 'песня')
print(donald.name,'ID: ',id(donald))#выводим ID выведенной памят для экземпляра/переменной donald
donald.sing()#Выводит Quack-quack!
del donald#В книге, это позволяет очистить память от экземпляра/переменной, но он это делает автоматически
pity = Songbird('Pity','Pity-pity!')
print(pity.name,'ID: ',id(pity))
pity.sing()
del pitty