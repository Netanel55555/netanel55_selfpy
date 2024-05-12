def temp_converter(temp):

    temp_value = int(temp[:len(temp)-1:])
    converted_value = None

    if temp[-1] == 'F':
        converted_value = (5 * temp_value - 160)/9

    elif temp[-1] == 'C':
        converted_value = (9 * temp_value + (32 * 5))/5

    else:
        print("ERROR")
        return -1

    return converted_value


temperature = input("Insert the temperature you would like to convert:")
print(temp_converter(temperature))