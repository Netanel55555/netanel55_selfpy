def is_greater(my_list, n):
    new_list = []

    for number in my_list:
        if number > n:
            new_list.append(number)

    return new_list


result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
