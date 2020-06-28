"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
# --== Python 3.8; OS x64 ==--

from memory_profiler import profile
from sys import getrefcount
from pympler import asizeof
from random import randint


@profile
def create_m(x, y):
    return [[randint(10, 100) for ii in range(x)] for i in range(y)]


@profile
def trans_m(m):
    tmp = [[] for i in m[0]]
    for i in m:
        for idx2, ii in enumerate(i):
            tmp[idx2].append(ii)
    return tmp


@profile
def main():
    m = create_m(500, 300)
    print('Ссылок на матрицу m: ', getrefcount(m))
    print(f'Размер Матрицы m = {asizeof.asizeof(m) // 1024} кб')
    mm = trans_m(m)
    print(f'Размер Транспонированной матрицы mm = {asizeof.asizeof(mm) // 1024} кб')
    print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', max([ii for ii in [min(i) for i in mm]]))
    print('Ссылок на матрицу m: ', getrefcount(m))
    print('Ссылок на матрицу mm: ', getrefcount(mm))
    id_m = id(m)
    print(m)
    del m
    del mm
    print('Ссылок на матрицу m: ', getrefcount(m))


main()
