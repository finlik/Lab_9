import random
print('Программа загадает случайное число от 1 до последнего числа, заданного пользователем'
while True:
    try:
        N = int(input('Введите последнее число диапазона: '))
        k = int(input('Введите количество попыток: '))
    except ValueError:
        print ('Вы ввели некорректное значение. Повторите попытку')
        continue
    number = random.randint(1, N)
    while k != 0:
        number_user = int(input('Введите число: '))
        k -= 1
        if number_user < number:
            print ('Ваше число меньше того, что загадала программа')
        if number_user > number:
            print ('Ваше число больше того, что загадала программа')
        if number_user == number:
            break
    if number_user == number:
        print ('Поздравляю! Вы угадали число!')
    else:
        print ('Попытки закончились. Программа загадала число {0}'.format(number))
    break
