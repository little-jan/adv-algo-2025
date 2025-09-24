def delightful(srted):
    length = len(srted)
    i = 0
    j = length - 1

    final_lst = []
    while i < j:
        final_lst.append(srted[j])
        final_lst.append(srted[i])
        i += 1
        j -= 1
    if i == j:
        final_lst.append(srted[j])
    return final_lst

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

length = int(input())
lst = list(map(int, input().split()))
quicksort(lst, 0, length - 1)
print(" ".join(map(str, delightful(lst))))