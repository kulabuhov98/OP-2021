# -- coding: utf-8 --

""" 
    Практическая работа: 1. Номер зачетной книжки: 21-677.
  
    Автор: Кулабухов Александр Максимович, ЗИТ-21
    Дата: 26.01.2022

    Задание 7. Проверьте является ли значение в переменной number - четным.
"""

print ("Введите число: ")
number = int(input())

if number % 2 == 0:
    print ("Введенное число " + str(number) + " является четным.")
else:
    print ("Введенное число " + str(number) + " является нечетным.")