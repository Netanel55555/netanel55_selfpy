def squared_numbers(start, stop):
    squared_list = []

    for i in range(start, stop + 1):  # Corrected range arguments
        squared_list.append(i * i)

    return squared_list  # Return the list


result = squared_numbers(-3, 3)
print(result)
