# -- coding: utf-8 --

""" 
    Практическая работа: 4. Номер зачетной книжки: 21-677.
  
    Автор: Кулабухов Александр Максимович, ЗИТ-21
    Дата: 26.01.2022

    Задание 4. Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. 
    Результат запишите в строку и выведите получившуюся строку. Решение задачи должно быть выполнено без использования конструкции if и ей подобных.
"""

sourceString = str(input("Введите строку: "))

def swapString(sourceString):
    splitString = sourceString.split(" ")
    print(splitString[1] + " " + splitString[0])

swapString(sourceString)