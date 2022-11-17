import logging
import random
logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logging.info('User started program')

print('Программа загадает случайное число от 1 до последнего числа, заданного пользователем')
logging.info(f'Programm printed "Программа загадает случайное число от 1 до последнего числа, заданного пользователем"')
while True: 
    try:
        N = int(input('Введите последнее число диапазона: '))
        logging.info(f'Users input {N}')
        
        k = int(input('Введите количество попыток: '))
        logging.info(f'Users input {k}')
    
    except ValueError:
        print ('Вы ввели некорректное значение. Повторите попытку')
        logging.error('Incorrect number')
        continue
    
    number = random.randint(1, N) #программа выбирает случайное число
    logging.info(f'Programm selects {number}')
    
    while k != 0: #пока число попыток не будет равно 0, пользователь будет отгадывать число
        number_user = int(input('Введите число: '))
        logging.info(f'Users input {number_user}')
        k -= 1 #вычитаем единицу при каждом вводе числа
        if number_user < number:
            print ('Ваше число меньше того, что загадала программа')
            logging.info(f'Programm printed "Ваше число меньше того, что загадала программа"')
        if number_user > number:
            print ('Ваше число больше того, что загадала программа')
            logging.info(f'Programm printed "Ваше число больше того, что загадала программа"')
        if number_user == number:
            break
    if number_user == number:
        print ('Поздравляю! Вы угадали число!')
        logging.info(f'Programm printed "Поздравляю! Вы угадали число!"')
    else:
        print ('Попытки закончились. Программа загадала число {0}'.format(number))
        logging.info(f'Programm printed "Попытки закончились"')
    logging.info('Programm ended')
    break
