import random


def one_iteration(l):
    is_sort = True

    for index in range(0, l.__len__() - 1):
        if l[index] > l[index + 1]:
            tmp = l[index]
            l[index] = l[index + 1]
            l[index + 1] = tmp

            is_sort = False
    return l, is_sort


def bubble_sort(l):
    is_sort = False

    while not is_sort:
        l, is_sort = one_iteration(l)
    return l


if __name__ == "__main__":
    init = [random.randint(0, 1000) for _ in range(0, 800)]
    l = bubble_sort(init)

    print(f'is sort: {l == sorted(init)}')
