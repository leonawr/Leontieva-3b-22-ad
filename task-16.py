class Cat:

    def __init__(self, name, ages, colour):
        self.name = name
        self.ages = ages
        self.colour = colour

    def get_info(self):
        print(f'Кошка по имени {self.name}, {self.ages} лет, цвет {self.colour}')


cat = Cat('Белла', 3, 'белый')
cat.get_info()
