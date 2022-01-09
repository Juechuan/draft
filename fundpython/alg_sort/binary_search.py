from fundpython.utils.util import get_random_list, swap


def binary_search(target, lyst):
    left = 0
    right = len(lyst) - 1

    while left <= right:
        midpoint = (right + left) // 2
        if target == lyst[midpoint]:
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


def selection_sort(lyst):
    i = 0
    while i < len(lyst) - 1:
        min_index = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            swap(lyst, i, j)


r = get_random_list(1, 10, 7)

print(r, binary_search(3, r))
