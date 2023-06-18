name = str(input('Введите имя файла: '))

try:
    with open(name, 'r') as file:
        i = file.read()
        print(i)

except FileNotFoundError:
    print('Ошибка')
    
except OSError:
    print('Ошибка')