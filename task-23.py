print('Введите число:')
a = int(input())
i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    i.index(a)
    print('Число найдено в массиве')
    
except ValueError:
    print('Число не найдено в массиве')
