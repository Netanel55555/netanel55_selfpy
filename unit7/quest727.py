def print_and_create(char, count):
    print_string = char * count

    print(print_string)


def arrow(my_char, max_length):
    i = 1

    while i < max_length:
        print_and_create(my_char, i)
        i += 1

    print_and_create(my_char, i)

    while i > 0:
        print_and_create(my_char, i)
        i -= 1


arrow('*', 100)
