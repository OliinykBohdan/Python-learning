class Movie:
    def __init__(self, title):
        self.title = title


class Moviegoer:
    def __init__(self, name):
        self.name = name


class Cinema:
    def __init__(self, total_seats, movie):
        self.total_seats = total_seats
        self.movie = movie
        self.seats_taken = []

    def reserve_place(self, goer):
        if len(self.seats_taken) >= self.total_seats:
            print('\nUnfortunately, we no longer have any places available.')
            return

        if goer in self.seats_taken:
            print('\nA seat has already been reserved for you at this cinema.')
            return

        print(f'Your seat has been reserved. Thank you, {goer.name}.')
        self.seats_taken.append(goer)

    def make_room(self, goer):
        if goer not in self.seats_taken:
            print('\nYou did not have a reservation.')
            return

        print(f'\nThe reservation has been canceled, {goer.name}.\n')
        self.seats_taken.remove(goer)

    def show_seats(self):
        print(f'\n{30 * '~'} \nMovie: {self.movie.title} \nThere are {self.total_seats - len(self.seats_taken)} seats available.\n{30 * '~'}')


moviegoer1 = Moviegoer('Ivan')
moviegoer2 = Moviegoer('Anton')
moviegoer3 = Moviegoer('Marina')
moviegoer4 = Moviegoer('Bohdan')

cinema = Cinema(3, Movie('Interstellar'))

cinema.show_seats()

cinema.reserve_place(moviegoer1)
cinema.reserve_place(moviegoer2)
cinema.reserve_place(moviegoer3)
cinema.reserve_place(moviegoer4)

cinema.show_seats()

cinema.make_room(moviegoer1)

cinema.reserve_place(moviegoer4)
cinema.reserve_place(moviegoer4)

cinema.show_seats()
