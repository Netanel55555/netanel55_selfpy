def mult_tuple(tuple1, tuple2):
    list_answer = []

    for first_number in tuple1:
        for second_nuber in tuple2:
            temp_list = (first_number, second_nuber)
            list_answer.append(temp_list)
            temp_list = (second_nuber, first_number)
            list_answer.append(temp_list)

    answer = tuple(list_answer)

    print(answer)


first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
mult_tuple(first_tuple, second_tuple)
