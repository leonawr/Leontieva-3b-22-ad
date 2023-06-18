try:
    with open('text.txt', 'r') as file:
        i = file.read()
        print(i)
        
except FileNotFoundError:
    print('Файл не найден')
