def knapsack(values, weights, maximum):
    n = len(values)
    dp = [[0 for x in range(maximum + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, maximum + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][maximum]


values = list(map(int, input("Enter the profit values: ").split()))
weights = list(map(int, input("Enter the weights: ").split()))
maximum = int(input("Enter maximum storage allocated: "))
max_value = knapsack(values, weights, maximum)
print(f"The maximum value of items that can be included in the knapsack is: {max_value}")
