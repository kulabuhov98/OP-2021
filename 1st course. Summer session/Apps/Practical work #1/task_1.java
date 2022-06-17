/*
 * Номер зачетной книжки: 21-677.
 *
 * Автор: Кулабухов Александр Максимович, ЗИТ-21
 * Дата: 16.06.2022
 *
 * Реализовать программу, получающую на вход в качестве аргумента имя человека 
 * и выводящую "Hello, " + имя + "!", в противном случае, если параметр 
 * не передавался, "Hello World!".
 */

package task_1;

public class task_1 {
    public static void main(String[] name) {
        if (name.length > 0) {
            System.out.print("Hello, " + name[0] + "!"); /* Сообщение пользователю */
        } else {
            System.out.print("Hello, World!"); /* Сообщение пользователю */
        }
    }
}