import random

def ascii_to_digit(char):
    return ord(char) - ord('0')


def atoi(string, magnitude=1):
    if len(string) == 1:
        return ascii_to_digit(string[-1]) * magnitude

    return atoi(string[:-1], magnitude * 10) + ascii_to_digit(string[-1]) * magnitude


if __name__ == "__main__":
    test_number = [random.randint(0, 100000) for _ in range(0, 100)]
    res_number = [atoi(str(elem)) for elem in test_number]

    isOk = [res == test for (res, test) in zip(test_number, res_number)]
    if False in isOk:
        print('false')
    else:
        print('ok')
