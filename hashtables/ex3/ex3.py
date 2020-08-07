def intersection(arrays):
    arrays_table = {}
    count = {}

    # build dictionary with all arrays
    for k, a in enumerate(arrays):
        arrays_table[k] = a

    # count number of times each integers shows up
    for k, a in arrays_table.items():
        for j in a:
            if j not in count:
                count[j] = 0
            count[j] += 1

    result = []

    # if number was in every array, add to result list
    for key, counts in count.items():
        if counts == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append([1, 2, 3, 4, 5])
    # arrays.append([12, 7, 2, 9, 1])
    # arrays.append([99, 2, 7, 1,])

    arrays.append([1])
    arrays.append([1])

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
