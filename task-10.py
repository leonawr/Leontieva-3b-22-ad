class Person:

    def __init__(self, name, ages):
        self.name = name
        self.ages = ages

    def get_info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.ages}')


pers = Person('Вероника', 19)
pers.get_info()
