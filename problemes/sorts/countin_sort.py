import random


def counting_sort(l):
    m_l = max(l)
    counting_l = [0 for _ in range(0, m_l + 1)]

    for elem in l:
        counting_l[elem] += 1

    final_list = []
    for counting_elem, index in zip(counting_l, range(0, counting_l.__len__())):
        final_list.extend([index for _ in range(0, counting_elem)])

    return final_list


if __name__ == "__main__":
    init = [random.randint(0, 1000) for _ in range(0, 800)]
    print(init)

    l = counting_sort(init)

    print(f'is sort: {l == sorted(init)}')
