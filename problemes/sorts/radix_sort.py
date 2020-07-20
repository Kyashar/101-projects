import random
from collections import deque

BUCKET_SIZE = 10


def radix_sort(l, power=1):
    final_list = deque()

    for elem in l:
        if elem & power:
            final_list.append(elem)
        else:
            final_list.appendleft(elem)

    return radix_sort(final_list, power ** 2)


if __name__ == "__main__":
    init = [random.randint(0, 1000) for _ in range(0, 800)]

    l = radix_sort(init)
    print(l)

    print(f'is sort: {l == sorted(init)}')