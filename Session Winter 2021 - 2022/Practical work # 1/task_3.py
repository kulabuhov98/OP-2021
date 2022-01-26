# -- coding: utf-8 --

""" 
    Практическая работа: 1. Номер зачетной книжки: 21-677.
  
    Автор: Кулабухов Александр Максимович, ЗИТ-21
    Дата: 26.01.2022

    Задание 3. В переменной age хранится возраст. Вывести на экран "Поздравляем вы поступили в ВГУИТ", если age больше или равно "16", или если age меньше 16 - "Сначала нужно окончить школу!".
        Проверить, что значение age больше 0 и меньше 75.
        Проверить, что поступающего зовут не Иван.
        Если Абитуериенту меньше 16 вывести на экран сколько лет ему еще учиться в школе.
"""

print ("Введите возраст: ")
age = int(input())

print ("Введите имя: ")
name = str(input())

if age < 16:
    print ("Сначала нужно окончить школу!")
    print ("Осталось учиться в школе: " + str(16-age) + " лет / год / года.")
else:
    print("Поздравляем Вы поступили в ВГУИТ!")

if age > 0 and age < 75:
    print ("Введенный возраст " + str(age) + ". Он находится в промежутке от 0 до 75.")
else:
    print ("Введенный возраст " + str(age) + ". Он не находится в промежутке от 0 до 75.")

if name != "Иван":
    print ("Введенное имя " + str(name) + ". К сожалению, Вы не Иван =(")
else:
    print ("Введенное имя " + str(name) + ". Поздравляем, Вы Иван =)")