try:
    with open('text.txt', 'r') as file:
        inner = file.read()
        print(inner)
except FileNotFoundError:
    print('Файл не найден')
