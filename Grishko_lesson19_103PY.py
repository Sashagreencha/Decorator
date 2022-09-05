# def decor(func):    # передаю в функцию декоратор в качестве аргумента func()
#     def wrapper(arg):
#         res_lst_d = []  # формирую один список из элементов вложенного списка
#         for a in arg:
#             for i in a:
#                 res_lst_d.append(i)
#         result = len(res_lst_d) - len(func(arg))    # разница между длинной общего списка и списка элементов кратных  3
#         return result
#     return wrapper
#
# @decor
# def func(lst_):
#
#     res_lst = []    # список эелментов кратных 3
#     for arg in lst_:
#         for i in arg:
#             if i % 3 == 0:
#                 res_lst.append(i)
#     return res_lst
#
# print(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

"""
Домашняя задача
"""


# def debug(func):  # передаю в функцию декоратор функцию sum_
#     def wrapper(*args):
#         res = func(*args)
#         print(f'Имя функции {func.__name__}, переменные {args}')
#
#         return res
#
#     return wrapper
#
#
# @debug
# def sum_(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# print(sum_(2, 4))
# print(sum_(4, 8))
