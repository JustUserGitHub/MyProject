from random import randint

n = int(input('Выберите максимальную границу игры: '))
print(randint(1, n), 'Добро пожаловать в числовую угадайку!', sep='\n')

def is_valid(num):
    return (num.isdigit() and int(num) in range(1, n + 1))

num = randint(1, n) # загаданное число
count = 0 # счётчик

while True:    
    attempt = input('Введите предполгаемое число: ') # попытка пользователя
    if is_valid(attempt):
        attempt = int(attempt)
        if attempt > num:
            print('Слишком много, попробуйте ещё раз')
            count += 1
        elif attempt < num:
            print('Слишком мало, попробуйте ещё раз')
            count += 1
        else:
            print('Вы угадали, поздравляем!', f'Количество попыток отгадать {count + 1}', sep='\n')
            answer = input('Сыграть в игру ещё раз? (да или нет): ')
            if answer[0] == 'н':            # завершение игры 
                print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')   
                break
            elif answer[0] == 'д':         # новая игра
                n = int(input('Выберите максимальную границу игры: '))       
                print(randint(1, n), 'Добро пожаловать в числовую угадайку!', sep='\n')
                num = randint(1, n)       # загаданное число
                count = 0
                continue
    else:
        print('A может быть всё-таки введём целое число от 1 до 100?')
        count += 1
        continue