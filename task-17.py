class Book:

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_info(self):
        print(f'{self.title}, {self.author} ({self.year}), {self.genre}')


book = Book('О дивный новый мир', 'Олдос Хаксли', 1932, 'антиутопия')
book.get_info()
