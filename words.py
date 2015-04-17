# -*- coding: utf-8 -*-

ALL_DICT = {
    # числа, порядок 1
    u'ноль': {'value': 0, 'type': 'digit', 'order': 1},
    u'нуль': {'value': 0, 'type': 'digit', 'order': 1},
    u'нуля': {'value': 0, 'type': 'sign', 'order': 0},
    u'нулей': {'value': 0, 'type': 'sign', 'order': 0},
    u'ноля': {'value': 0, 'type': 'sign', 'order': 0},
    u'нолей': {'value': 0, 'type': 'sign', 'order': 0},
    u'один': {'value': 1, 'type': 'digit', 'order': 1},
    u'одна': {'value': 1, 'type': 'digit', 'order': 1},
    u'единица': {'value': 1, 'type': 'sign', 'order': 0},
    u'единиц': {'value': 1, 'type': 'sign', 'order': 0},
    u'единицы': {'value': 1, 'type': 'sign', 'order': 0},
    u'единичка': {'value': 1, 'type': 'sign', 'order': 0},
    u'единичек': {'value': 1, 'type': 'sign', 'order': 0},
    u'два': {'value': 2, 'type': 'digit', 'order': 1},
    u'две': {'value': 2, 'type': 'digit', 'order': 1},
    u'двойка': {'value': 2, 'type': 'sign', 'order': 0},
    u'двоек': {'value': 2, 'type': 'sign', 'order': 0},
    #'двух': {'value': 2, 'type': 'digit', 'order': 1},
    #'дважды': {'value': 2, 'type': 'digit', 'order': 1},
    u'три': {'value': 3, 'type': 'digit', 'order': 1},
    #'трех': {'value': 3, 'type': 'digit', 'order': 1},
    #'трижды': {'value': 3, 'type': 'digit', 'order': 1},
    u'четыре': {'value': 4, 'type': 'digit', 'order': 1},
    #'четырех': {'value': 4, 'type': 'digit', 'order': 1},
    #'четырежде': {'value': 4, 'type': 'digit', 'order': 1},
    u'пять': {'value': 5, 'type': 'digit', 'order': 1},
    #'пяти': {'value': 5, 'type': 'digit', 'order': 1},
    u'шесть': {'value': 6, 'type': 'digit', 'order': 1},
    #'шести': {'value': 6, 'type': 'digit', 'order': 1},
    u'семь': {'value': 7, 'type': 'digit', 'order': 1},
    u'семерки': {'value': 7, 'type': 'sign', 'order': 0},
    u'семерка': {'value': 7, 'type': 'sign', 'order': 0},
    u'семерок': {'value': 7, 'type': 'sign', 'order': 0},
    u'семёрки': {'value': 7, 'type': 'sign', 'order': 0},
    u'семёрка': {'value': 7, 'type': 'sign', 'order': 0},
    u'семёрок': {'value': 7, 'type': 'sign', 'order': 0},
    #'семи': {'value': 7, 'type': 'digit', 'order': 1},
    u'восемь': {'value': 8, 'type': 'digit', 'order': 1},
    #'восьми': {'value': 8, 'type': 'digit', 'order': 1},
    u'девять': {'value': 9, 'type': 'digit', 'order': 1},
    #'девяти': {'value': 9, 'type': 'digit', 'order': 1},

    # числа, порядок 1
    u'десять': {'value': 10, 'type': 'digit', 'order': 2},
    #'десяти': {'value': 10, 'type': 'digit', 'order': 1},
    u'одиннадцать': {'value': 11, 'type': 'digit', 'order': 2},
    #'одинадцати': {'value': 11, 'type': 'digit', 'order': 1},
    u'двенадцать': {'value': 12, 'type': 'digit', 'order': 2},
    #'двенадцати': {'value': 12, 'type': 'digit', 'order': 1},
    u'тринадцать': {'value': 13, 'type': 'digit', 'order': 2},
    #'тренадцати': {'value': 13, 'type': 'digit', 'order': 1},
    u'четырнадцать': {'value': 14, 'type': 'digit', 'order': 1},
    #'четырнадцати': {'value': 14, 'type': 'digit', 'order': 1},
    u'пятнадцать': {'value': 15, 'type': 'digit', 'order': 1},
    #'пятнадцати': {'value': 15, 'type': 'digit', 'order': 1},
    u'шестнадцать': {'value': 16, 'type': 'digit', 'order': 1},
    #'шестнадцати': {'value': 16, 'type': 'digit', 'order': 1},
    u'семнадцать': {'value': 17, 'type': 'digit', 'order': 1},
    #'семнадцати': {'value': 17, 'type': 'digit', 'order': 1},
    u'восемнадцать': {'value': 18, 'type': 'digit', 'order': 2},
    #'восемнадцати': {'value': 18, 'type': 'digit', 'order': 1},
    u'девятнадцати': {'value': 19, 'type': 'digit', 'order': 1},
    #'девятнадцать': {'value': 19, 'type': 'digit', 'order': 1},

    # числа, порядок 2
    u'двадцать': {'value': 20, 'type': 'digit', 'order': 2},
    #'двадцати'{'value': 20, 'type': 'digit', 'order': 2},
    u'тридцать': {'value': 30, 'type': 'digit', 'order': 2},
    #'тридцати'{'value': 30, 'type': 'digit', 'order': 2},
    u'сорок': {'value': 40, 'type': 'digit', 'order': 2},
    #'сорока'{'value': 40, 'type': 'digit', 'order': 2},
    u'пятьдесят': {'value': 50, 'type': 'digit', 'order': 2},
    #'пятидесяти'{'value': 50, 'type': 'digit', 'order': 2},
    u'шеcтьдесят': {'value': 60, 'type': 'digit', 'order': 2},
    #'шестидесяти'{'value': 60, 'type': 'digit', 'order': 2},
    u'семьдесят': {'value': 70, 'type': 'digit', 'order': 2},
    #'семидесяти'{'value': 70, 'type': 'digit', 'order': 2},
    u'восемьдесят': {'value': 80, 'type': 'digit', 'order': 2},
    #'восьмидесяти'{'value': 80, 'type': 'digit', 'order': 2},
    u'девяносто': {'value': 90, 'type': 'digit', 'order': 2},
    #'девяноста'{'value': 90, 'type': 'digit', 'order': 2},

    # числа, порядок 3
    u'сто': {'value': 100, 'type': 'digit', 'order': 3},
    u'сотня': {'value': 100, 'type': 'digit', 'order': 3},
    u'двести': {'value': 200, 'type': 'digit', 'order': 3},
    u'триста': {'value': 300, 'type': 'digit', 'order': 3},
    u'четыреста': {'value': 400, 'type': 'digit', 'order': 3},
    u'пятьсот': {'value': 500, 'type': 'digit', 'order': 3},
    u'шестьсот': {'value': 600, 'type': 'digit', 'order': 3},
    u'семьсот': {'value': 700, 'type': 'digit', 'order': 3},
    u'восемьсот': {'value': 800, 'type': 'digit', 'order': 3},
    u'девятьсот': {'value': 900, 'type': 'digit', 'order': 3},

    # кванторы порядка
    u'десятка': {'value': 10, 'type': 'degree', 'order': 2},
    u'десятков': {'value': 10, 'type': 'degree', 'order': 2},
    u'сотни': {'value': 100, 'type': 'degree', 'order': 3},
    u'сотен': {'value': 100, 'type': 'degree', 'order': 3},
    u'тысяча': {'value': 1000, 'type': 'degree', 'order': 4},
    u'тысячи': {'value': 1000, 'type': 'degree', 'order': 4},
    u'тысяч': {'value': 1000, 'type': 'degree', 'order': 4},
    u'миллионов': {'value': 1000000, 'type': 'degree', 'order': 7},
    u'миллион': {'value': 1000000, 'type': 'degree', 'order': 7},
    u'миллиона': {'value': 1000000, 'type': 'degree', 'order': 7},
    u'миллиард': {'value': 1000000000, 'type': 'degree', 'order': 10},
    u'миллиарда': {'value': 1000000000, 'type': 'degree', 'order': 10},
    u'миллиардов': {'value': 1000000000, 'type': 'degree', 'order': 10},
}


def convert(string):
    """
    Конвертирует словесное представление в число

    :param string: строка
    :return: целое число, которое удалось получить из строки
    """
    res = 0
    degree = 0
    for token in string.split():
        operand = None
        if token in ALL_DICT:
            operand = ALL_DICT[token]
        else:
            try:
                number = int(token)
                operand = {'value': number, 'type': 'digit', 'order': len(str(number))}
            except TypeError:
                pass

        if operand:
            if operand['type'] == 'degree' and res == 0:
                operand['type'] = 'digit'

            if operand['type'] == 'degree':
                res *= operand['value']
            elif operand['type'] == 'sign':
                last_digit = res % 10
                res /= 10
                if operand['value'] == 0:
                    res *= 10**last_digit
                else:
                    for i in xrange(last_digit):
                        res *= 10
                        res += operand['value']
            elif degree > operand['order']:
                res += operand['value']
            else:
                res = res * 10 ** operand['order'] + operand['value']
            degree = operand['order']
        else:
            break
    return res
