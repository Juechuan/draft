from fundpython.utils.util import get_random_list


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


r = get_random_list(1, 10, 7)

print(r, binary_search(3, r))
