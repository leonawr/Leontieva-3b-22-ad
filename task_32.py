class Pupil:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(f'Школьник {self.name} учится')


pupil = Pupil('Катя', 13)
pupil.study()
