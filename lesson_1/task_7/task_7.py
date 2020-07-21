
year = int(input('Введите год: '))
if not year % 4:
    print(str(year)+' - высокосный год')
else:
    print(str(year) + ' -  не высокосный год')
