import sys

attempt_pin = 0

print('===== Welcome to the ATM =====')

# PIN authentication (max 3 attempts)
while attempt_pin < 3:
    pin = input('Please enter a pin: ')

    if pin == '1122':
        print('Access granted')
        break
    else:
        print('Pin not recognised')
        attempt_pin += 1

# Exit if authentication failed
if attempt_pin == 3:
    print('Access denied')
    sys.exit()

balance = 1000.0

menu = '''
Choose an option:
1 - Check balance
2 - Deposit
3 - Withdraw
4 - Exit
'''

# Main ATM menu loop
while True:
    print(menu)
    choice = input('Enter your choice: ')

    if choice == '1':
        print(f'Your balance: {balance}')

    elif choice == '2':
        while True:
            am_depos = input('Enter the amount to deposit or exit: ')

            if am_depos == 'exit':
                break

            # Prevent ValueError
            try:
                amount = float(am_depos)

                if amount <= 0:
                    print('\nAmount must be positive.')
                else:
                    balance += amount
                    print(f'\nDeposit successful. Your new balance is: {balance}')

            except ValueError:
                print('\nPlease enter a valid number or type "exit".')

    elif choice == '3':
        while True:
            withdraw = input('Enter the withdrawal amount or exit: ')

            if withdraw == 'exit':
                break

            try:
                amount = float(withdraw)

                if amount <= 0:
                    print('\nAmount must be positive.')
                # Prevent overdraft
                elif balance < float(withdraw):
                    print('\nTransaction failed: not enough balance.')
                else:
                    balance -= float(withdraw)
                    print(f'\nWithdrawal successful. Your remaining balance is: {balance}')

            except ValueError:
                print('\nPlease enter a valid number or type "exit".')

    elif choice == '4':
        print ('=== Thank you. Goodbye. ===')
        break

    else:
        print('Please enter a valid option.')