def backpack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


def backpack2(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[-1]


def full_backpack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[-1]


def multi_backpack(weights, values, capacity, nums):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            for k in range(1, nums[i] + 1):
                if j >= k * weights[i]:
                    dp[j] = max(dp[j], dp[j - k * weights[i]] + k * values[i])
    return dp[-1]


def multi_backpack2(weights, values, capacity, nums):
    weights = []
    values = []
    capacity = 8
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[-1]


weights = [2, 3, 4]
values = [3, 4, 5]
nums = [2, 1, 2]
capacity = 8

print(backpack(weights, values, capacity))
print(backpack2(weights, values, capacity))
print(full_backpack(weights, values, capacity))
print(multi_backpack(weights, values, capacity, nums))
print(multi_backpack2(weights, values, capacity, nums))
