from models.user import User
from models.account import Account


def login(users):
    print('===== Welcome to the ATM =====')

    verification_name = input('Please enter your name: ')

    current_user = None

    for user in users:
        if verification_name == user.username:
            current_user = user
            break

    if current_user is None:
        print('Invalid username. Please try again.')
        return None

    attempts = 0
    attempts_allowed = 3

    while attempts < 3:
        verification_pin = input('Please enter your pin: ')

        if current_user.check_pin(verification_pin):
            print(f'\nWelcome back, {current_user.username}!')
            print('~~~Access granted~~~')

            return current_user

        attempts += 1
        attempts_allowed -= 1

        print(f'Invalid pin. {attempts_allowed} attempts left.')

    print('\nAccess denied!')
    return None


def show_menu():
    return '''
Choose an option:
1 - Check balance
2 - Deposit
3 - Withdraw
4 - Exit
'''


def main():
    account1 = Account(3000)
    account2 = Account(5000)

    user1 = User('Bohdan', '1111', account1)
    user2 = User('Victoria', '2222', account2)

    users = [user1, user2]

    current_user = login(users)

    if current_user is None:
        return

    while True:
        print(show_menu())

        choice = input('Enter your choice: ')

        if choice == '1':
            print(f'Your balance: {current_user.account.balance}')

        elif choice == '2':

            try:
                amount = float(input('Enter deposit amount: '))

                current_user.account.deposit(amount)
                print(f'Your new balance: {current_user.account.balance}')

            except ValueError:
                print('Please enter a positive number.')

        elif choice == '3':

            try:
                amount = float(input('Enter withdraw amount: '))

                current_user.account.withdraw(amount)
                print(f'Your new balance: {current_user.account.balance}')

            except ValueError:
                print('Please enter a positive number.')

        elif choice == '4':
            print('=== Thank you. Goodbye. ===')
            break

        else:
            print('Please enter a valid choice.')


if __name__ == '__main__':
    main()
