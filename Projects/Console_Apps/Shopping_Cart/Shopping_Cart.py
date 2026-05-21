store = {
    'orange' : 25.0,
    'potato' : 53.0,
    'apple' : 33.0,
}
price = {
    'orange' : 5.0,
    'potato' : 2.0,
    'apple' : 3.0,
}
cart = {}

menu = '''
=== Shopping Cart ===
1. Add product
2. Show cart
3. Remove product
4. Total price
5. Exit
'''

while True:
    print(menu)
    choice = input('Enter your choice: ')

    if choice == '1':
        while True:
            print('\n~~~ Items in stock (the price is per 1 kg) ~~~')
            for product in store:
                print(f'{product}: {price[product]} $ | {store[product]} kg available')

            choice_product = input('Select an item or exit: ')

            if choice_product == 'exit':
                break
            elif choice_product not in store:
                print('This item is not available.')
                continue

            try:
                quantity = float(input('Enter the quantity in kg: '))

            except ValueError:
                print('Please enter a numeric value.')
                continue

            if quantity <= 0:
                print('Please enter a positive number.')
                continue

            elif quantity > store[choice_product]:
                print('Sorry, we do not have that many items in stock.')
            else:
                cart[choice_product] = cart.get(choice_product, 0) + quantity
                store[choice_product] -= quantity
                print('Thank you, the item has been added to your cart.')

    elif choice == '2':
        if cart == {}:
            print('The cart is empty.')
        else:
            print('~~~ Items in your cart ~~~')
            for product, weight in cart.items():
                print(f'{product}: {weight} kg')

    elif choice == '3':
        while True:
            if cart == {}:
                print('The cart is empty.')
                break
            else:
                print('~~~ Items in your cart ~~~')
                for key, value in cart.items():
                    print(f'{key}: {value} kg')
                all_remove = input('Do you want to delete all these items? (y/n): ')

                if all_remove == 'y':
                    cart = {}
                    print('All items have been removed from your cart.\n')
                    break

                elif all_remove == 'n':
                    remove_product = input('Please enter what you want to remove or exit: ')
                    if remove_product == 'exit':
                        break

                    elif remove_product not in cart:
                        print('Sorry, this item is not in your cart.\n')
                        continue

                    try:
                        remove_weight = float(input('Enter the weight in kg: '))

                    except ValueError:
                        print('Please enter a numeric value.\n')
                        continue

                    if remove_weight <= 0:
                        print('Please enter a positive number.\n')
                        continue

                    elif remove_weight >= cart[remove_product]:
                        store[remove_product] += cart[remove_product]
                        del cart[remove_product]
                        print('The selected item has been removed.\n')
                    else:
                        cart[remove_product] -= remove_weight
                        store[remove_product] += remove_weight
                        print('The weight of the selected item has been reduced.\n')

                else:
                    print('Please enter a valid choice.\n')

    elif choice == '4':
        if cart == {}:
            print('The cart is empty.')
        else:
            total_price = 0
            for product, weight in cart.items():
                total_price += weight * price[product]
            print(f'\nTotal price: {total_price} $')

    elif choice == '5':
        print('=== Thank you. Goodbye. ===')
        break

    else:
        print('Please enter a valid choice.')