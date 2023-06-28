# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
# Пример:
#
# Ввод:
#
# 1/2
# 1/3
# Вывод:
#
# 5/6 1/6


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(num, den):
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor


def add_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2

    num = num1 * den2 + num2 * den1
    den = den1 * den2

    return simplify_fraction(num, den)


def multiply_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2

    num = num1 * num2
    den = den1 * den2

    return simplify_fraction(num, den)


def main():
    fraction1 = input("Введите первую дробь в формате a/b: ")
    fraction2 = input("Введите вторую дробь в формате a/b: ")

    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    frac1 = (num1, den1)
    frac2 = (num2, den2)

    sum_fraction = add_fractions(frac1, frac2)
    print(f"Сумма: {sum_fraction[0]}/{sum_fraction[1]}")

    product_fraction = multiply_fractions(frac1, frac2)
    print(f"Произведение: {product_fraction[0]}/{product_fraction[1]}")


if __name__ == '__main__':
    main()
