import random
from collections import deque

BUCKET_SIZE = 10


def __radix_sort(l, power, m):
    if m < power:
        return l

    t_list = deque()
    f_list = deque()
    for elem in l:
        if power & elem:
            t_list.append(elem)
        else:
            f_list.append(elem)

    f_list.extend(t_list)
    return __radix_sort(f_list, power << 1, m)


def radix_sort(l):
    power = 1
    m = max(l)

    return __radix_sort(l, power, m)


if __name__ == "__main__":
    init = [random.randint(0, 1000) for _ in range(0, 800)]

    print(init)
    l = list(radix_sort(init))

    print(l)
    print(f'is sort: {l == sorted(init)}')