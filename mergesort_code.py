def merge(lst, left, mid, right):
    s1, s2 = (mid - left + 1), (right - mid)
    L, R = (lst[left:mid + 1]), (lst[mid + 1:right + 1])

    i, j, k = 0, 0, left

    while i < s1 and j < s2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    while i < s1:
        lst[k] = L[i]
        i, k = i + 1, k + 1

    while j < s2:
        lst[k] = R[j]
        j, k = j + 1, k + 1

def mergesort(lst, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(lst, left, mid)
        mergesort(lst, mid + 1, right)
        merge(lst, left, mid, right)

