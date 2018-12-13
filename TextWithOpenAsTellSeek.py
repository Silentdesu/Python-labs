text = 'The political slogan "Workers Of The World Unite!" is from The Communist Manifesto.'
with open('update.txt','w') as file: #с with open('твой любой файл.txt') as любое имя переменной ты можешь открыть файл и он автоматически закрывается
	file.write(text)
	print("\nFile now closed?",file.closed)
print('File now closed?',file.closed)
with open('update.txt','r+') as file:
	text = file.read()
	print('\nString: ',text)
	print('\nPosition in file now: ',file.tell()) #Показывает на какой позиции стоит курсор
	position = file.seek(33) #Перемещает позицию на такой-то индекс и можно делать изменения
	print('Position in file now: ',file.tell())
	file.write('All Lands')
	file.seek(59)
	file.write('The tombstone of Kari Marx.')
	file.seek(0)#Нулевой индекс означает,что переходит в самое начало строки текста
	text = file.read()#И выводит весь текст
	print('\nString: ',text)