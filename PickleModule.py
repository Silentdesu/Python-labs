import pickle
import os

if not os.path.isfile('pickle.dat'): #Если файла pickle.dat нету в моей директории(Ex:Desktop)
	data = [0, 1]#Создаем словарь с двумя ключами
	data[0] = input('Enter topic: ')#Первый ключ
	data[1] = input('Enter series: ')#Второй ключ
	file = open('pickle.dat','wb')#Создаем переменную и файл picke.dat в режиме запись в биннарном виде
	pickle.dump(data, file)#При помощи модуля pickel и метода dump записываем все с клавиатуры в файл 
	file.close()закрываем файл
else:#Если все-таки файл есть в нашей директории
	file = open('pickle.dat','rb')#То создаем переменную,которая открывает файл в режиме чтения биннарного вида
	data = pickle.load(file)#Возвращает из биннарного в человеческий текст и сохраняет в переменной data
	file.close()
	print('Welcome back to: ' + data[0] + data[1])#Вывод текста
