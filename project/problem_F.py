def partition_finder(lst):
    sum_lst = sum(lst)
    len_lst = len(lst)
    mid = len_lst // 2
    p1 = lst[:mid]
    p2 = lst[mid + 1:]
    