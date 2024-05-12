from collections import deque


def shift_left(my_list):
    temp_list = deque(my_list)
    temp_list.rotate(-1)
    return list(temp_list)


result = shift_left([0, 1, 2])
print(result)
