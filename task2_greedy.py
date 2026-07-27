def greedy(A, m, n):
    # Task 2: Greedy - O(m * n)

    # A= array, size m*n (m= rows (stocks), n= columns (days))
    max_profit = -1
    best_stock = 0
    best_buy = 0
    best_sell = 0

    for i in range(1, m + 1):  # Go through every stock
        if n < 2:    # If less than 2 days, skip stock
            continue

        min_price = A[i - 1][0]  # Start with day 1
        min_day = 1
        local_max_profit = 0
        local_buy = 1
        local_sell = 1

        for j in range(2, n + 1):  # Single pass over days starting from day 2
            current_profit = A[i - 1][j - 1] - min_price   # Profit if you sell today using best buy so far
            if current_profit > local_max_profit:   # Update local best if better
                local_max_profit = current_profit
                local_buy = min_day
                local_sell = j

            if A[i - 1][j - 1] < min_price:   # Update minimum price and day if today is cheaper than previous min
                min_price = A[i - 1][j - 1]
                min_day = j

        if local_max_profit > max_profit:   # Compare and update this stock's best with global best
            max_profit = local_max_profit
            best_stock = i
            best_buy = local_buy
            best_sell = local_sell

    if max_profit > 0:
        return (best_stock, best_buy, best_sell, max_profit)
    else:
        return (0, 0, 0, 0)