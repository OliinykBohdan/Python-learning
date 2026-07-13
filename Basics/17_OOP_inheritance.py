class Bild:
    def __init__(self, years, city):
        self.years = years
        self.city = city

        self.get_info()

    def get_info(self):
        print('Year:', self.years, 'City:', self.city)


class School(Bild):
    def __init__(self, years, city, pupils):
        super(School, self).__init__(years, city)
        self.pupils = pupils


class House(Bild):
    pass


class Shop(Bild):
    pass


school = School(1973, 'Dnipro', 500)
house = Bild(1985, 'Kyiv')
shop = Bild(1999, 'Odesa')
