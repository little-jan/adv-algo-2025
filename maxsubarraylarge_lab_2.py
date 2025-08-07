def subarray_sum(lst, left, mid, right):
    best_left = 0
    total = 0
    for lwr in range(mid, left - 1, -1):
        total += lst[lwr]
        if total > best_left:
            best_left = total

    best_right = 0
    total = 0
    for lwr in range(mid + 1, right + 1):
        total += lst[lwr]
        if total > best_right:
            best_right = total

    return best_left + best_right

def divconq(lst, left, right):
    if left == right:
        return lst[left]
    mid = (left + right) // 2
    left_sum = divconq(lst, left, mid)
    right_sum = divconq(lst, mid + 1, right)
    cross = subarray_sum(lst, left, mid, right)
    return max(left_sum, right_sum, cross)

def max_subarray(xs: list[int]) -> int:
    xs = [int(val) for val in xs]
    result = max(divconq(xs, 0, len(xs)-1), 0)
    return result

input()
test = input().split()
sum = max_subarray(test)
print(sum)