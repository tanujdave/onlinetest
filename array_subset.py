def get_subset_for_sum(arr, k):

    print(arr, k)

    if len(arr) == 0:
        return None

    if arr[0] == k:
        return [arr[0]]

    with_first = get_subset_for_sum(arr[1:], k - arr[0])
    print(with_first)
    if with_first:
        return [arr[0]] + with_first
    else:
        return get_subset_for_sum(arr[1:], k)


print(get_subset_for_sum([12, 1, 61, 5, 9, 2], 24))

