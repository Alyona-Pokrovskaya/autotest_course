# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    letters = string.ascii_lowercase
    while True:
        first_word_length = random.randint(1, 15)
        second_word_length = random.randint(1, 15)
        first_word = "".join(random.choice(letters) for i in range(first_word_length))
        second_word = "".join(random.choice(letters) for i in range(second_word_length))
        yield f'{first_word} {second_word}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
