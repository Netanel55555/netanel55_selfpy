from ordered_set import OrderedSet


def sort_anagrams(list_of_strings):
    sorted_set = OrderedSet("".join(sorted(word)) for word in list_of_strings)

    sorted_len = len(sorted_set)
    answer = [[] for _ in range(sorted_len)]

    for string in list_of_strings:
        index = sorted_set.index("".join(sorted(string)))
        answer[int(index)].append(string)

    return answer


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless',
                 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
my_list = sort_anagrams(list_of_words)

print(my_list)
