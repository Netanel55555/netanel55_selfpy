from itertools import chain


def extend_list_x(list_x, list_y):
    list_x = list(chain(list_y, list_x))
    print(list_x)


x = [4, 5, 6]
y = [1, 2, 3]

extend_list_x(x, y)
