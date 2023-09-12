# Десятичное в двоичное
# Условие
# На вход подается число в десятичной системе счисления
# ● Задача
# Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную
# систему счисления. Обоснуйте сделанный выбор парадигм.

def to_base(number: int, base: int = 2):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXXYZ"
    binary_num = []
    while number:
        binary_num.append(digits[number % base])
        number //= base
    return "".join(reversed(binary_num))


print(to_base(26, 16))
