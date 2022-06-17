/*
 * Вариант: 20. Номер зачетной книжки: 21-677.
 *
 * Автор: Кулабухов Александр Максимович, ЗИТ-21
 * Дата: 17.06.2022
 *
 * Задача 1. Определить одномерный массив и заполнить его случайными значениями:
 * Дан массив из 16 двоичных цифр (0;1). Определить сколько раз в этом массиве 
 * меняется число 0 на 1 или 1 на 0. Например, в массиве 11110010001101 число меняется 6 раза.
 */

package task_1;

import java.security.SecureRandom; /* Класс криптографической генерации случайных чисел */

public class task_1 {
	public static void main(String[] args) {
		SecureRandom secureRandom = new SecureRandom(); /* Объект класса */
		int array[] = new int[16]; /* Инициализация одномерного массива из 16 двоичных цифр */
		int count = 0; /* Количество изменений числа 0 на 1 или 1 на 0 */
		
		System.out.println("Массив из 16 двоичных цифр (0;1):"); /* Сообщение пользователю */
		for (int i = 0; i < 16; i++) { /* Цикл по столбцам */
			array[i] = secureRandom.nextInt(2 - 0) + 0; /* Заполнение одномерного массива случайными двоичными цифрами (0;1) */
			System.out.print(array[i] + " "); /* Сообщение пользователю */
		}
		
		for (int i = 1; i < 16; i++) { /* Цикл по столбцам */
			if (array[i] != array[i - 1]) { /* Определяем, сколько раз в одномерном массиве меняется число 0 на 1 или 1 на 0 */
				count++; /* Количество изменений числа 0 на 1 или 1 на 0 */
			}
		}
		System.out.print("\nВ этом массиве меняется число 0 на 1 или 1 на 0: " + count + " раз!"); /* Сообщение пользователю */
	}
}