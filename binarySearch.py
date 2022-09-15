def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1


def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        return binary_search_recursive(numbers_list, number_to_find, mid_index + 1, right_index)
    else:
        return binary_search_recursive(numbers_list, number_to_find, left_index, mid_index - 1)


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 9809

    index1 = binary_search(numbers_list, number_to_find)
    index2 = linear_search(numbers_list, number_to_find)
    index3 = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"Number found at index {index1} using binary search")
    print(f"Number found at index {index2} using linear search")
    print(f"Number found at index {index3} using recursive binary search")
