from random import randint


def get_random_list(begin, end, length):
    if length > 0:
        list_length = int(length)
    else:
        list_length = 0
    if begin <= end:
        list_begin, list_end = begin, end
    else:
        list_begin, list_end = end, begin

    random_list = []
    for i in range(list_length):
        random_list.append(randint(list_begin, list_end))
    return random_list
