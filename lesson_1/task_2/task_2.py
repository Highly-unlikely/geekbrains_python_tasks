# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки

print('Введите две координаты')
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
if x1 == x2:
    if y1 == y2:
        print('Вы ввели координаты точки')
    else:
        print('x = ' + str(x1))
else:
    print('y = ' + str((y2-y1)/(x2-x1)) + 'x + (' + str((x2*x1-x1*y2)/(x2-x1))+')')