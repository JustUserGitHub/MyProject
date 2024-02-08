n = int(input('Шаг сдвига: ')) # сдвиг шифра
direction = input('Направление (шифрование или дешифрование): ')
language = input('Язык алфавита (русский или английский): ') # язык сообщения 
text = input('Введите текст: ')# закодированное или декодированное сообщение

ru_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
en_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

if language == 'english' or language == 'ENGLISH' or language == 'English' or language == 'английский' or language == 'АНГЛИЙСКИЙ' or language == 'Английский':
    if direction == 'шифрование' or direction == 'ШИФРОВАНИЕ' or direction == 'Шифрование':
        t = ''
        for c in text: 
            if c.isalpha():
                c = en_letters[en_letters.find(c) + n]    
            t += c
        print(t, end='')
    elif direction == 'дешифрование' or direction == 'ДЕШИФРОВАНИЕ' or direction == 'Дешифрование':
        t = ''
        en_letters_reverse = en_letters[::-1]
        for c in text:
            if c.isalpha():
                c = en_letters_reverse[en_letters_reverse.find(c) + n]    
            t += c
        print(t, end='')
        
elif language == 'русский' or language == 'РУССКИЙ' or language == 'Русский':
    if direction == 'шифрование' or direction == 'ШИФРОВАНИЕ' or direction == 'Шифрование':
        t = ''
        for c in text: 
            if c.isalpha():
                c = ru_letters[ru_letters.find(c) + n]    
            t += c
        print(t, end='')
    elif direction == 'дешифрование' or direction == 'ДЕШИФРОВАНИЕ' or direction == 'Дешифрование':
        t = ''
        ru_letters_reverse = ru_letters[::-1]
        for c in text: 
            if c.isalpha():
                c = ru_letters_reverse[ru_letters_reverse.find(c) + n]    
            t += c
        print(t, end='')