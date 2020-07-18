import heapq


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
    dq = []
    for c in string:
        if c in dq:
            dq = list(filter(c.__ne__, dq))
        else:
            dq.append(c)

    return dq[0]


if __name__ == "__main__":
    first_c = find_first_non_repeated_with_dic("stritnsg")
    print(first_c)
    first_c = find_first_non_repeated("stritnsg")
    print(first_c)

