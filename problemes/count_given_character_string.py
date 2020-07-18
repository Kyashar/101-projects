def count_char(string, character):
    count = 0
    for c in string:
        count = count + 1 if character == c else count

    return count


if __name__ == "__main__":
    pass
