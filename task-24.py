class Employee:

    def __init__(self, name, ages, salary):
        self.name = name
        self.ages = ages
        self.salary = salary

    def view(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.ages}')
        print(f'Зарплата: {self.salary}')


emp = Employee('Вероника', 19, 500000)
emp.view()
