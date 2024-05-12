def inverse_dict(my_dict):
    new_dict = dict()

    keys_list = list(my_dict.keys())
    values_list = list(my_dict.values())
    values_list.sort(reverse=True)

    for value in values_list:
        new_dict[value] = []

    for key in keys_list:
        new_dict[my_dict[key]].append(key)

    return new_dict


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict).items())
