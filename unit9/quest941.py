from ordered_set import OrderedSet


def choose_word(file_path, index) -> tuple:
    with open(file_path, "r") as file:
        file_data = file.read()
    lines = file_data.split("\n")

    file_list = []
    for line in lines:
        file_list.extend(line.split())

    unique_words = list(set(file_list))  
    count = len(unique_words)

    if not (0 <= index < count):
        raise IndexError(f"Index {index} out of range for {count} unique words")

    chosen_word = unique_words[index] 
    return (count, chosen_word)
