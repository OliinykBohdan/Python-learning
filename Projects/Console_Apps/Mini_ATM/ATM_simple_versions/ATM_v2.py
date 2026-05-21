def pin_authentication():
    attempt_pin = 0

    while attempt_pin < 3:
        pin = input('Please enter a pin: ')
        if pin == '1122':
            return True
        else:
            attempt_pin += 1
            print('Pin not recognised')

    return False


def show_menu():
    return '''
Choose an option:
1 - Check balance
2 - Deposit
3 - Withdraw
4 - Exit
'''


def deposit(balance):
    while True:
        amount_deposit = input('Enter amount (q to quit): ')

        if amount_deposit.lower() == 'q':
            return balance

        try:
            amount = float(amount_deposit)

            if amount <= 0:
                print('\nAmount must be positive.')
            else:
                balance += amount
                print(f'\n===Deposit successful===\nYour new balance is: {balance}')

        except ValueError:
            print('\nPlease enter a valid number or q to quit')


def withdraw(balance):
    while True:
        withdraw_amount = input('Enter amount (q to quit): ')

        if withdraw_amount.lower() == 'q':
            return balance

        try:
            amount = float(withdraw_amount)

            if amount <= 0:
                print('\nAmount must be positive.')
            elif amount > balance:
                print('\nTransaction failed: not enough balance.')
            else:
                balance -= amount
                print(f'\n===Withdraw successful===\nYour new balance is: {balance}')

        except ValueError:
            print('\nPlease enter a valid number or q to quit')


def main():
    print('===== Welcome to the ATM =====')

    if not pin_authentication():
        print('\nAccess denied')
        return

    print('\n~~~Access granted~~~')

    balance = 1000.0

    while True:
        print(show_menu())
        choice = input('Enter your choice: ')

        if choice == '1':
            print(f'Your balance: {balance}')
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print('=== Thank you. Goodbye. ===')
            break
        else:
            print('\nPlease enter a valid choice.')

if __name__ == "__main__":
    main()