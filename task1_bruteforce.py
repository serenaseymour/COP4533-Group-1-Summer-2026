def brute_force(A, m, n):
    # Task 1: Brute Force - O(m * n^2)

    # A= array, size m*n (m= rows (stocks), n= columns (days))
    max_profit = -1
    best_stock = 0
    best_buy = 0
    best_sell = 0

    for i in range(1, m + 1):  # Go through every stock
        for j1 in range(1, n + 1):  # Try every possible buy day
            for j2 in range(j1 + 1, n + 1):  # Try every later sell day
                profit = A[i - 1][j2 - 1] - A[i - 1][j1 - 1]   # Calculate profit
                if profit > max_profit:   # Track the best transaction seen so far, and update
                    max_profit = profit
                    best_stock = i
                    best_buy = j1
                    best_sell = j2

    if max_profit > 0:   # Return the best valid positive profit transaction
        return (best_stock, best_buy, best_sell, max_profit)
    else:
        return (0, 0, 0, 0)