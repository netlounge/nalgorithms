def counting_sort(collection):

    # if the collection is empty, returns empty
    if collection == []:
        return []

    # get some information about the collection
    coll_len = len(collection)
    coll_max = max(collection)
    coll_min = min(collection)

    # create the counting array
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # count how much a number appears in the collection
    for number in collection:
        counting_arr[number - coll_min] += 1

    print(counting_arr)

    # sum each position with it's predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the collection
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    print(counting_arr)
    # create the output collection
    ordered = [0] * coll_len

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered


def counting_sort_string(string):
    """
    >>> counting_sort_string("thisisthestring")
    'eghhiiinrsssttt'
    """
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


if __name__ == "__main__":
    arr = [1, 4, 1, 2, 7, 5 ,2]
    print(counting_sort(arr))
    