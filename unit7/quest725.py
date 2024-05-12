from ordered_set import OrderedSet


def sequence_del(my_str):
    my_set = OrderedSet()

    for char in my_str:
        my_set.add(char)

    print(''.join(my_set))


sequence_del("SSSSsssshhhh")
# sequence_del("Heeyyy   yyouuuu!!!")
