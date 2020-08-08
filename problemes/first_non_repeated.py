def find_first_non_repeated_with_dic(string):
    dic = {}
    for c, index in zip(string, range(0, len(string))):
        if c in dic:
            dic[c]['count'] += 1
        else:
            dic[c] = {'count': 1, 'index': index}

    l = [(key, elem['index']) for key, elem in dic.items() if elem['count'] == 1]
    return sorted(l, key=lambda elem: elem[1])[0][0]


def find_first_non_repeated(string):
    nr = []
    re = []
    for c in string:
        if c in nr:
            nr = list(filter(c.__ne__, nr))
            re.append(c)
        elif c not in re:
            nr.append(c)

    if len(nr) > 0:
        return nr[0]
    return None


if __name__ == "__main__":
    first_c = find_first_non_repeated_with_dic("strinsgttrrin")
    print(first_c)
    first_c = find_first_non_repeated("strinsgttrri")
    print(first_c)

