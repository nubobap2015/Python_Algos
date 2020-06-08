"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

print('Введите координаты 2х точек X,Y')
X1 = float(input('Введите X1: '))
Y1 = float(input('Введите Y1: '))
X2 = float(input('Введите X2: '))
Y2 = float(input('Введите Y2: '))
print(
    f'Уравнение полученной прямой y = {(Y2-Y1)/(X2-X1):.3f}x + {Y2 - ((Y2-Y1)/(X2-X1))*X2:.3f}')
