def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j+1]:
                swap(j, j+1, elements)
                swapped = True
        if not swapped:
            break


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while end >= 0 and elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor


def merge(a, b, elements):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            elements[k] = a[i]
            i += 1
        else:
            elements[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        elements[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        elements[k] = b[j]
        j += 1
        k += 1


def merge_sort(elements):
    if len(elements) <= 1:
        return
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, elements)


def shell_sort(elements):
    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j-gap] > anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2


def selection_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if elements[j] < elements[min_index]:
                min_index = j

        if i != min_index:
            swap(i, min_index, elements)


if __name__ == '__main__':
    numbers = [5, 9, 2, 1, 67, 34, 88, 34]
    numbers1 = [11, 9, 29, 7, 2, 15, 28]
    numbers2 = [10, 3, 15, 7, 8, 23, 98, 29]
    numbers3 = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    numbers4 = [78, 12, 15, 8, 61, 53, 23, 27]
    cases = [
        [],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5],
        [29, 15, 28]
    ]

    bubble_sort(numbers)
    quick_sort(numbers1, 0, len(numbers1) - 1)
    insertion_sort(numbers1)
    merge_sort(numbers2)
    shell_sort(numbers3)
    selection_sort(numbers4)
    for case in cases:
        quick_sort(case, 0, len(case) - 1)
        print(f"Sort case result: {case}")

    print(f"Bubble sort result: {numbers}")
    print(f"Quick sort result: {numbers1}")
    print(f"Insertion sort result: {numbers1}")
    print(f"Merge sort result: {numbers2}")
    print(f"Shell sort result: {numbers3}")
    print(f"Selection sort result: {numbers4}")
