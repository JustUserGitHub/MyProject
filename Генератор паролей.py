from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = '!#$%&*+-=?@^_'
chars = ''
count = int(input('Введите количество паролей: '))
lenght = int(input('Введите длину пароля: '))
digit = input('Включать ли цифры 0123456789? (да или нет) - ')
lowercase_letter = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да или нет) - ')
uppercase_letter = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да или нет) - ')
punctuation = input('Включать ли символы !#$%&*+-=?@^_? (да или нет) - ')
exceptions = input('Исключать ли неоднозначные символы il1Lo0O? (да или нет) - ')
if digit[0].lower() == 'д':
    chars += digits
if lowercase_letter[0].lower() == 'д':
     chars += lowercase_letters
if uppercase_letter[0].lower() == 'д':
     chars += uppercase_letters
if punctuation[0].lower() == 'д':
    chars += punctuations
if exceptions[0].lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
def generate_password(lenght, chars):
    return sample(chars, lenght)
for _ in range(count):
    print(*generate_password(lenght, chars), sep='')