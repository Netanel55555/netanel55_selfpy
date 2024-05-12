def are_files_equal(file1, file2):
    answer = True
    input_file_one = open(file1, "r")
    input_file_two = open(file2, "r")

    for line_file1, line_file2 in input_file_one, input_file_two:

        if line_file1 != line_file2:
            answer = False
            break

    input_file_one.close()
    input_file_two.close()
    return answer