import random

word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]

def get_word():
    return random.choice(word_list)

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
                ''' 
                   |  
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
                '''

                                   
                         
                

                   -
                '''
    ]
    return stages[tries]

def play(word):
    word = get_word()
    tries = 9
    guessed_letters = []
    letters = []
    word_completion = '_' * (len(word))
    print('Давайте играть в угадайку слов!')
    print(f'У Вас {tries} попыток.')
    print(display_hangman(tries))
    print('Загаданное слово:', * word_completion)
    print()

    while True:
        if tries > 0:
            word_input = input('Введите букву или слово: ')
            print()
            if word_input.isalpha(): # проверяем введённую попытку пользователя
                if len(word_input) == 1: # пользователь ввёл букву
                    if word_input in letters:
                        print('Такая буква уже была введена ранее. Введите новую.') 
                        print()
                        continue
                    letters.append(word_input)
                    if word_input not in word: # буквы нет в загаданном слове
                        tries -= 1
                        print(f'Такой буквы нет в слове. У Вас {tries} попыток.')
                        print(display_hangman(tries))
                        continue
                    else:
                        t = ''
                        if word_input in word:
                            guessed_letters.append(word_input)
                        for char in word:
                            if char in guessed_letters:
                                t += char.upper()
                            else:
                                t += '_'
                        print('Загаданное слово:', * t)
                        print()
                        if t.isalpha():
                            print('Поздравляем, вы угадали слово! Вы победили!')
                            print()
                            word_input = input('Сыграть в игру ещё раз? (да или нет): ')
                            if  word_input[0] == 'н' or word_input[0] == 'Н':            # завершение игры 
                                print('Спасибо, что играли в угадайку слов. Ещё увидимся...')   
                                break
                            elif word_input[0] == 'д' or word_input[0] == 'Д':         # новая игра
                                word = get_word()
                                tries = 9
                                guessed_letters = []
                                letters = []
                                word_completion = '_' * (len(word))
                                print('Давайте играть в угадайку слов!')
                                print(f'У Вас {tries} попыток.')
                                print(display_hangman(tries))
                                print('Загаданное слово:', * word_completion)
                                print()
                                continue
                elif len(word_input) > 1: # пользователь ввёл слово
                    if word_input in letters:
                        print('Такое слово уже было введено ранее. Введите новое.') 
                        print()
                        continue
                    letters.append(word_input)
                    if word == word_input:
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        print()
                        word_input = input('Сыграть в игру ещё раз? (да или нет): ')
                        if  word_input[0] == 'н' or word_input[0] == 'Н':            # завершение игры 
                            print('Спасибо, что играли в угадайку слов. Ещё увидимся...')   
                            break
                        elif word_input[0] == 'д' or word_input[0] == 'Д':         # новая игра
                            word = get_word()
                            tries = 9
                            guessed_letters = []
                            letters = []
                            word_completion = '_' * (len(word))
                            print('Давайте играть в угадайку слов!')
                            print(f'У Вас {tries} попыток.')
                            print(display_hangman(tries))
                            print('Загаданное слово:', * word_completion)
                            print()
                            continue
                    else: # слова не совпадают по длине
                        tries -= 1
                        print(f'Введённое слово не совпало. У Вас {tries} попыток.')
                        print(display_hangman(tries))
                        continue
                    if word_input in guessed_letters:
                        print('Такая буква уже была введена ранее')
                        print()
                        continue
            else: # предлагаем пользователяю ввести только символы из букв
                print('A может быть всё-таки введём букву или слово?!')
                print()
                continue
        elif tries == 0: # закончилось кол-во попыток отгадать
            print('Вы проиграли!'f' Загаданным словом было "{word.upper()}"')
            print()
            word_input = input('Сыграть в игру ещё раз? (да или нет): ')
            print()
            if  word_input[0] == 'н' or word_input[0] == 'Н':            # завершение игры 
                print('Спасибо, что играли в угадайку слов. Ещё увидимся...')   
                break
            elif word_input[0] == 'д' or word_input[0] == 'Д':         # новая игра
                word = get_word()
                tries = 9
                guessed_letters = []
                letters = []
                word_completion = '_' * (len(word))
                print('Давайте играть в угадайку слов!')
                print(f'У Вас {tries} попыток.')
                print(display_hangman(tries))
                print('Загаданное слово:', * word_completion)
                print()
                continue
play(get_word())