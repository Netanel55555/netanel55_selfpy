def contain_seven(number):
    return '7' in str(number)


def divisible_by_seven(number):
    return 7 * int(number / 7) == number


def seven_boom(end_number):
    new_list = []
    for number in range(0, end_number+1, 1):
        if divisible_by_seven(number) or contain_seven(number):
            new_list.append("BOOM")
        else:
            new_list.append(str(number))

    return new_list


print(seven_boom(17))