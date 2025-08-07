def max_sum_subarray_better(xs: list[int]) -> int:
    best = 0
    for lwr in range(len(xs)):
        total = 0
        for i in range(lwr, len(xs)):
            total += xs[i]
            best = max(best, total)
    return best

input()
test = input().split()
test = [int(val) for val in test]
max_sum = max_sum_subarray_better(test)
print(max_sum)
