class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

    def print_sentence(self):
        print('"{}" by {} ({}) hangs in the {}.'.format(self.title, self.painter, self.year, self.museum))


cuadro = Painting(input(), input(), input())
cuadro.print_sentence()
