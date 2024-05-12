from collections import OrderedDict

from ordered_set import OrderedSet

EXIT = 9


def print_cart(cart):
    print(', '.join(cart))


def print_number_of_products(cart):
    print(len(cart))


def is_item_in_cart(cart):
    product = input("Please enter a product name: ")
    if product in cart:
        print(f"Yes, there's {product}  in this cart")
    else:
        print(f"No, there's no {product}  in this cart")


def count_of_product_in_cart(cart):
    product = input("Please enter a product name: ")

    product_count = cart.count(product)

    if product_count:
        print(f"There's {product} {product}  in this cart")
    else:
        print(f"There's no {product}  in this cart")


def remove_product_from_cart(cart):
    product = input("Please enter a product name: ")

    if product in cart:
        cart.remove(product)

        print(f"{product}  was removed form the cart")

    else:
        print(f"There's no {product}  in this cart")


def add_product_to_cart(cart):
    product = input("Please enter a product name: ")

    cart.append(product)


def print_illegal_products(cart):
    illegal_products = []

    for product in cart:
        if len(product) < 3 or not product.isalpha():
            illegal_products.append(product)

    print(''.join(illegal_products))


def remove_duplicates_products(cart):
    cart_set = OrderedDict.fromkeys(cart)

    cart[:] = list(cart_set)


def ask_for_service(service_id, cart):
    function_list = [print_cart, print_number_of_products, is_item_in_cart, count_of_product_in_cart,
                     remove_product_from_cart, add_product_to_cart, print_illegal_products, remove_duplicates_products]

    function_list[service_id - 1](cart)


def supermarket_bot(shopping_cart):
    grocery_list = shopping_cart.split(",")
    while True:
        service_id = input("Please enter a service id: ")

        if int(service_id) == EXIT:
            break

        elif int(service_id) > EXIT:
            print("Service id goes from 1 - 9, please try again")
            continue

        ask_for_service(int(service_id), grocery_list)

    print("Goodbye, we hope you've enjoyed")


my_cart = "Milk,Cottage,Tomatoes"
supermarket_bot(my_cart)
