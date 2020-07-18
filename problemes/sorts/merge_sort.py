import random


def fusion_lists(list_1, list_2):
    if not list_1:
        return list_2
    if not list_2:
        return list_1

    if list_1[0] > list_2[0]:
        return [list_2[0]] + fusion_lists(list_1, list_2[1:])
    return [list_1[0]] + fusion_lists(list_1[1:], list_2)


def merge_sort(l):
    if l.__len__() > 1:
        half = int(l.__len__() / 2)
        return fusion_lists(
            merge_sort(l[:half]),
            merge_sort(l[half:])
        )

    return l


if __name__ == "__main__":
    init = [random.randint(0, 1000) for _ in range(0, 800)]
    print(init)

    l = merge_sort(init)

    print(l)
    print(f'is sort: {l == sorted(init)}')
