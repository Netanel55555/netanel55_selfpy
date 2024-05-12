def who_is_missing(file_name):
    missing_num = 0
    with open(file_name, 'r') as file:
        numbers_str = file.read().strip()  # Read and remove extra whitespace

    numbers = [int(num) for num in numbers_str.split(',')]

    for i in range(1, len(numbers) + 1):
        if numbers[i - 1] != i:
            missing_num = i

    with open("/home/netanel55/PycharmProjects/sigitSelfHomework/ found.txt", "w") as missing_num_file:
        missing_num_file.write(str(missing_num))

    print(missing_num)