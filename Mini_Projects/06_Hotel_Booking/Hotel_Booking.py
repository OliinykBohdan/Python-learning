class User:
    def __init__(self, name):
        self.name = name


class Room:
    def __init__(self, number):
        self.number = number
        self.guest = None
        self.is_available = True


class HotelBooking:
    def __init__(self):
        self.all_rooms = []

    def add_room(self, room):
        self.all_rooms.append(room)

    def chek_in(self, room, user):
        if room.guest is not None:
            print(f'Room №{room.number} is already taken. {user.name}, please choose another room.')
            return

        room.guest = user
        room.is_available = False
        print(f'{user.name} has checked into room №{room.number}.')

    def check_out(self, room):
        if room.guest is None:
            print(f'\nThe room №{room.number} is unoccupied.')
            return

        print(f'\nThe room №{room.number} has been vacated.')
        room.guest = None
        room.is_available = True

    def show_all_rooms(self):
        print(10 * '=', 'All rooms', 10 * '=', sep='\n')
        for room in self.all_rooms:
            status = 'Available' if room.is_available else 'Occupied'
            print(f'Room {room.number} - {status}')


hotel = HotelBooking()

room1 = Room(1)
room2 = Room(2)
room3 = Room(3)

user1 = User('Bohdan')
user2 = User('Olha')
user3 = User('Stepan')

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

hotel.chek_in(room1, user1)
hotel.chek_in(room2, user2)
hotel.chek_in(room2, user3)

hotel.show_all_rooms()

hotel.check_out(room2)
hotel.check_out(room3)

hotel.show_all_rooms()
