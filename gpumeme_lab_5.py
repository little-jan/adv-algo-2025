# def knapsack(capacity, items):
#     dpt = [float('inf')] * (capacity + 1)
#     dpt[0] = 0
#
#     for wi, vi in items:
#         for j in range(capacity, -1, -1):
#             if dpt[j] != float('inf'):
#                 new_env = j + vi
#                 if new_env <= capacity:
#                     dpt[new_env] = min(dpt[new_env], dpt[j] + wi)
#
#     max_env = 0
#     cheapest = float('inf')
#     for env_cost in range(capacity + 1):
#         if dpt[env_cost] != float('inf'):
#             if env_cost > max_env:
#                 max_env = env_cost
#                 cheapest = dpt[env_cost]
#             elif env_cost == max_env:
#                 cheapest = min(cheapest, dpt[env_cost])
#
#     return cheapest
#
#
# print(knapsack(6, [(2, 3), (3, 3), (1,4)]))

def knapsack(W, val, wt):
    dp = [(-1, float('inf'))] * (W + 1)
    dp[0] = (0, 0)    # tuple format is (env cost, money cost)

    for i in range(1, len(wt) + 1):
        for j in reversed(range(W, wt[i - 1] - 1)):
            prev_env, prev_money = dp[j - wt[i - 1]]

            if prev_env != -1:
                new_env, new_money = prev_env + wt[i - 1], prev_money + val[i]
                current_env, current_money = dp[j]
                if new_env > current_env or (new_env == current_env and new_money < current_money):
                    dp[j] = (new_env, new_money)

    best_env, best_money = -1, float('inf')
    for k in range(len(dp)):
        env, money = dp[k]
        if env <= W:
            if env > best_env or (env == best_env and money < best_money):
                best_env, best_money = env, money

    return best_money

print(knapsack(10, [1, 1, 2, 3], [11, 9, 1, 1]))


# import heapq
#
# def knapsack(capacity: int, items: list[tuple[int, int]]) -> int:
#     dpt = []
#
#     for wi, vi in items:
#         heapq.heappush(dpt, (wi, vi))
#         for i in range(len(items)):
#             print(items[i])
#             new_w = wi + items[i][0]
#             new_v = vi + items[i][1]
#             heapq.heappush(dpt, (new_w, new_v))
#
#     print(dpt)
#     cheapest = float('inf')
#     largest = float('-inf')
#     while dpt:
#         w, v = heapq.heappop(dpt)
#         print(w, v)
#         if v > capacity:
#             continue
#         else:
#             if v == capacity:
#                 largest = v
#                 cheapest = w
#                 break
#             elif v > largest:
#                 largest = v
#                 cheapest = w
#
#
#     return cheapest
#
# print(knapsack(10, [(1, 11), (1, 9), (2, 1), (3, 1)]))