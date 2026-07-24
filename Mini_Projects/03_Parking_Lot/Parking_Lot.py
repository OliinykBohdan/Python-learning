class User:
    def __init__(self, name):
        self.name = name


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_users = []

    def park_user(self, user):
        if user in self.parked_users:
            print(f'{user.name} is already parked.')
            return

        if len(self.parked_users) >= self.capacity:
            print('There are no free parking spaces.')
            return

        self.parked_users.append(user)
        print(f'{user.name} parked successfully.')

    def remove_user(self, user):
        if user not in self.parked_users:
            print(f'\n{user.name} is not in the parking lot.')
            return

        self.parked_users.remove(user)
        print(f'\n{user.name} left the parking lot.')

    def show_available_spaces(self):
        print(f'\nAvailable parking spaces: {self.capacity - len(self.parked_users)}')

    def users_in_car_park(self):
        print('\nUsers in the car park:')
        if not self.parked_users:
            print('No cars in the parking lot.')
            return

        for user in self.parked_users:
            print(user.name)


parking_lot = ParkingLot(3)

user1 = User('John')
user2 = User('Jane')
user3 = User('Julia')
user4 = User('Mike')

parking_lot.park_user(user1)
parking_lot.park_user(user2)
parking_lot.park_user(user3)
parking_lot.park_user(user4)

parking_lot.users_in_car_park()

parking_lot.remove_user(user2)

parking_lot.users_in_car_park()

parking_lot.show_available_spaces()
