def knapsack(W, val, wt):
    dp = [(-1, float('inf'))] * (W + 1)
    dp[0] = (0, 0)

    for i in range(1, len(wt) + 1):
        for j in range(W, wt[i - 1] - 1, -1):
            prev_env, prev_money = dp[j - wt[i - 1]]

            if prev_env != -1:
                new_env, new_money = prev_env + wt[i - 1], prev_money + val[i-1]
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

lines, W = input().split()
W = int(W)
vals = []
wt = []

for i in range(int(lines)):
    val, w = input().split()
    vals.append(int(val))
    wt.append(int(w))

print(knapsack(W, vals, wt))