from ordered_set import OrderedSet


def count_chars(my_str):
    my_dict = dict()
    char_set = OrderedSet(my_str)

    for char in char_set:
        if char != " ":
            my_dict[char] = my_str.count(char)

    return my_dict


magic_str = "abra cadabra"
print(count_chars(magic_str).items())