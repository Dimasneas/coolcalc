from __future__ import division
import re
from math import sqrt, factorial, log10, log
from typing import Tuple

import coolcalc.settings as glob

sqrt_sign = u"\u221a"

MATH_SIGNS = ['+', '*', '/', '-', '^']
MATH_FUNCTIONS = ["log", "ln", sqrt_sign, 'abs']
MATH_ACTIONS = ['!', '%']
NUM_SYS = ['dec', 'bin', 'ter', 'qua', 'fiv', 'six', 'sep', 'oct']


def change_num_sys(x: int, base: int) -> int:
    """
    Перевод из десятичной системы счисления в другую
    :param x: число в десятичной записи.
    :param base: основание системы счисления.
    :return: Число в системе счисления base
    """

    t = 1
    d = 0
    while x > 0:
        d = d + (x % base) * t
        t = t * 10
        x = x // base
    return d


def factorial_expr(expr: str) -> Tuple[int, str]:
    """
    Выбирает выражение которое должно вычисляться под знаком факториала
    :param expr: выражение для поиска.
    :returns: Возвращает кортеж (начальная позиция выражения, вычисляемое выражение)
    """

    sign_ids = []
    last_sign = expr[-1]
    exp_len = len(expr)
    if last_sign in MATH_SIGNS:
        expr = expr[:-1]

    # Нахождение всех знаков
    for sign in MATH_SIGNS:
        sign_ids += list(i for i in range(len(expr)) if expr.startswith(sign, i))
    sign_ids.sort()

    # Нахождение всех скобок
    stack = []
    bracket = []
    for i, c in enumerate(expr):
        if c == "(":
            stack.append(i)
        elif c == ")":
            idx = stack.pop()
            bracket.append([idx, i])

    # Нахождение вложенных скобок и знаков в них
    signs = []
    for i in sign_ids:
        s = []
        for pair in bracket:
            if pair[0] < i < pair[1]:
                s.append(i)
        if i not in s:
            signs.append(i)
    signs.sort()

    #  Проверка существования знаков
    if signs:
        start = max(signs) + 1
    else:
        start = 0
    expr = expr[start:]

    if last_sign in MATH_SIGNS:
        start = exp_len + 1

    return start, expr


def normalize(expr: str) -> Tuple[str, str]:
    """
    Исправляет ошибки в выражении. Между скобками и числом добавляет знак умножить,
    добавляет открывающиеся скобки после начала функций(корень, модуль, логарифм),
    заменяет повторяющиеся знаки(+, -, *, /) на последний знак из последовательности,
    если необходимо добавляет перед знаками и в пустые скобки 0.
    Вычисляет основание системы счисления
    :param expr: выражение для обработки.
    :return: Возвращает кортеж (обработанное выражение, основание системы счисления)
    """

    if not expr:
        return '', ''
    num_sys = ""

    # Нахождение системы счисления
    for n_sys in NUM_SYS:
        if not num_sys and expr.startswith(n_sys):
            num_sys = n_sys
            expr = expr[3:]
        expr = expr.replace(n_sys, '')

    print(f"системы счисления: {expr}")
    # Добавление знаков и скобок к функциям
    result_expr = ''
    for func in MATH_FUNCTIONS:
        parts = expr.split(func)
        if len(parts) <= 1:
            continue
        i = 0
        print(parts)
        for part in parts:
            if not part or part[0] != '(':
                part = '(' + part
            if part[len(part) - 1] not in MATH_SIGNS and i != len(parts) - 1 and part != '(':
                part = part + '*'
            if i != 0:
                result_expr += func + part
            else:
                result_expr += part
            i += 1
    if result_expr:
        expr = result_expr

    print(f"знаки и функции: {expr}")
    # Добавление к открывающимся скобкам знаков умножения
    result_expr = ""
    parts = expr.split('(')
    prev_part = parts[0]
    cur = ""
    for i in range(1, len(parts)):
        cur = parts[i]
        if prev_part and (prev_part[-1].isdigit() or prev_part[-1] in MATH_ACTIONS + [')']):
            prev_part += "*"
        elif cur and cur[0] in MATH_SIGNS + MATH_ACTIONS + [')']:
            cur = '0' + cur
        result_expr += prev_part + '('
        prev_part = cur
    if result_expr:
        expr = result_expr + cur
    print(f"скобки: {expr}")
    # Закрытие всех скобок
    while expr.count("(") > expr.count(")"):
        expr += ")"
    print(f"закрытие скобок: {expr}")
    # Добавление к закрывающимся скобкам 0 и знаков умножения
    result_expr = ""
    parts = expr.split(')')
    prev_part = parts[0]
    cur = ""
    for i in range(1, len(parts)):
        cur = parts[i]
        if cur and cur[0].isdigit():
            cur = '*' + cur
        if prev_part and prev_part[-1] in MATH_SIGNS:
            prev_part += '0'
        result_expr += prev_part + ')'
        prev_part = cur
    if result_expr:
        expr = result_expr + cur
    print(f"обработ скобки: {expr}")
    # Удаление цепочек знаков
    result_expr = ""
    pattern = fr'[{"".join(re.escape(sym) for sym in MATH_SIGNS)}]+'
    copy = expr
    parts = re.findall(pattern, copy)
    for part in parts:
        i = copy.find(part)
        copy = copy.replace(part, part[-1], 1)
        result_expr += copy[:i + 1]
        copy = copy[i + 1:]
    if result_expr:
        expr = result_expr + copy
    print(f"знаки: {expr}")
    # Добавление 0 в начало, если там нет цифры
    if expr and expr[0] in MATH_SIGNS:
        expr = "0" + expr

    print(f"Нормализованное: {expr}")

    return expr, num_sys


def replace_math(expr: str) -> str:
    """
    Заменяет математические знаки и символы на выражения Python
    :param expr: вычисляемое выражение.
    :return: Возвращает выражение с функциями Python
    """
    if not expr:
        return ''

    replaces = {
        "^": "**",
        u"\u221a": "sqrt",
        "log": "log10",
        "ln": "log",
        "%": "/100",
    }

    # Заменяет некоторые знаки и функции на выражения питон
    for key, value in replaces.items():
        expr = expr.replace(key, value)

    # Заменяет "!" на функцию factorial
    f = expr.find('!')
    while f >= 0:
        start, s = factorial_expr(expr[:f])
        expr = f'{expr[:start]}factorial({s}){expr[f + 1:]}'
        f = expr.find('!')

    # Удаление лишних пустых скобок
    expr = expr.replace('()', '')

    return expr


def calculate(expr: str) -> str:
    """
    Считает выражение, и обрабатывает ошибки
    :param expr: Вычисляемое выражение.
    :return: Результат вычислений в оформленном виде
    """
    if not expr:
        return ''
    print("calc: " + expr)

    expr, num_sys = normalize(expr)
    expr = replace_math(expr)

    print(expr)

    try:
        result = eval(expr)
        if num_sys and num_sys != 'dec':
            if not isinstance(result, int):
                raise ValueError
            result = change_num_sys(result, NUM_SYS.index(num_sys)+1)
        if len(str(result)) > 18:
            result = f"{result:.10e}"
        elif float(result).is_integer():
            result = f"{int(result)}"
        elif len(str(result)) > 10:
            result = f"{round(result, 10):.10f}"
        else:
            result = str(result)
    except ValueError:
        result = glob.error_text["value"]
    except ZeroDivisionError:
        result = glob.error_text["zero_division"]
    except OverflowError:
        result = glob.error_text["overflow"]
    except (SyntaxError, NameError):
        result = glob.error_text["syntax"]
    except TypeError:
        result = ""
    return result
