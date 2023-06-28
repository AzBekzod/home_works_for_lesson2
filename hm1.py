# Напишите программу, которая получает целое число и  возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.


def decimal_to_hex(decimal):
    hex_chars = "0123456789ABCDEF"

    if decimal == 0:
        return "0"

    hex_str2 = ""   # Указал hex_str2, т.к. выдавал ошибку (Shadows name 'hex_str')
    negative = False

    if decimal < 0:
        negative = True
        decimal = abs(decimal)

    while decimal > 0:
        remainder = decimal % 16
        hex_str2 = hex_chars[remainder] + hex_str2
        decimal //= 16

    if negative:
        hex_str2 = "-" + hex_str2

    return hex_str2


number = int(input("Введите целое число: "))
hex_str = decimal_to_hex(number)
print("Шестнадцатеричное представление числа:", hex_str)
