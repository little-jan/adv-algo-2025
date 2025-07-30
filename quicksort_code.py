def pivot(val1, val2, val3):
    if (val1 <= val2 <= val3) or (val3 <= val2 <= val1):
        return val2
    elif (val2 <= val1 <= val3) or (val3 <= val1 <= val2):
        return val1
    else:
        return val3

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def partition(lst, first, last):
    mid = (first + last) // 2
    pivot_value = pivot(lst[first], lst[mid], lst[last])

    if pivot_value == lst[mid]:
        swap(lst, mid, last)
    elif pivot_value == lst[first]:
        swap(lst, first, last)

    pivot_index = last
    pivot_value = lst[pivot_index]

    i = first - 1
    for j in range(first, last):
        if lst[j] < pivot_value:
            i += 1
            swap(lst, i, j)

    swap(lst, i + 1, pivot_index)
    return i + 1

def quicksort(lst, first, last):
    if first < last:
        pi = partition(lst, first, last)
        quicksort(lst, first, pi - 1)
        quicksort(lst, pi + 1, last)

input()
test = input().split()
test = [int(val) for val in test]
quicksort(test, 0, len(test) -1)
print(test)
