# Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
# Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение
# типов не сработало


def get_sum(num_one, num_two):
    sum = int(num_one) + int(num_two)
    print(sum)


try:
    get_sum(1234.9932, '3332')
    get_sum('sdlksdlksdl', '3332')
    get_sum(123+3.44, 12/3.99)
except ValueError:
    print('Не все переменные - цифры!1')
