import random


def remove_duplicates(l):
    return list(set(l))


if __name__ == "__main__":
    init = [random.randint(0, 5) for _ in range(0, 10)]
    print(init)
    l = remove_duplicates(init)
    print(l)

