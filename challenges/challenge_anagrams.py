def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def is_anagram(first_string: str, second_string: str):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    first_arr = [x.lower() for x in first_string]
    second_arr = [x.lower() for x in second_string]

    quickSort(first_arr, 0, len(first_string) - 1)
    quickSort(second_arr, 0, len(second_string) - 1)

    anagram = first_arr == second_arr
    return (
        "".join([str(x) for x in first_arr]),
        "".join([str(x) for x in second_arr]),
        anagram,
    )
