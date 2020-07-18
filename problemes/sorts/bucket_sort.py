import random
from problemes.sorts.merge_sort import merge_sort

BUCKET_SIZE = 10


def bucket_sort(l):
    buckets = [[] for _ in range(0, max(l) // BUCKET_SIZE + 1) ]

    for elem in l:
        buckets[elem//BUCKET_SIZE].append(elem)

    final_list = []
    for bucket, index in zip(buckets, range(0, len(buckets))):
        final_list.extend(merge_sort(bucket))

    return final_list


if __name__ == "__main__":
    init = [random.randint(0, 1000) for _ in range(0, 800)]
    print(init)

    l = bucket_sort(init)

    print(l)
    print(sorted(init))
    print(f'is sort: {l == sorted(init)}')
