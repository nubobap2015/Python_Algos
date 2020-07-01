"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import random
from random import randint
from timeit import timeit


def create_list_int(list_len, l_border, r_border):
    return [randint(l_border, r_border - 1) for _ in range(list_len * 2 + 1)]


def get_median(base_list):
    for idx, val in enumerate(base_list):
        cnt1 = 0
        cnt2 = -1
        for idx2, val2 in enumerate(base_list):
            if val2 < val:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == cnt2:
            return val
    return None


a = create_list_int(5,0,10)
print(a)
print(sorted(a))
print(get_median(a))
