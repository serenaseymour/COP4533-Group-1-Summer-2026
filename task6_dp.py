def dp(A, m, n, c):
    # Task 6: Dynamic Programming - O(m*n^2)

    DP = [0] * n # stores max profit up to day d
    Choice = [None] * n # stores choices made during each day. either "skip" or (stock, buy_day, sell_day)

    if n<2: #if there are less than 2 days, no full transactions can be made
        return []

    for d in range(1, n+1): # for each day
        if d == 1: # on day 1, the profit is zero, no profitable transactions can be made
            DP[d-1] = 0
            Choice[d-1] = "skip" 

        else:
            DP[d-1] = DP[d-2] # on day 2 or later, option 1 is to skip day d and not sell
            Choice[d-1] = "skip"

            # option 2 is to sell on day d - check all stocks and previous buy days that adhere to the cooldown period
            for i in range(1, m+1): # for each stock
                for j in range(1, d): # for each buy day (exclude last day)
                    if (j-c-1) >= 1: # ensure that we only check valid buy days that adhere to the cooldown period

                        # max profit from previous eligible sell day + max profit from selling on day d
                        # takes into account the cooldown period from the previous sell day
                        current_total_profit = DP[j-c-2] + (A[i-1][d-1] - A[i-1][j-1])
                        
                    else:
                        current_total_profit = A[i-1][d-1] - A[i-1][j-1]

                    if current_total_profit > DP[d-1]: # checks if it is more profitable to skip day d or to sell on day d
                        DP[d-1] = current_total_profit
                        Choice[d-1] = (i, j, d)

    if DP[n-1] == 0:
        return [] # if the max profit is zero, return an empty list

    result = BuildSolution(Choice, n, c) # return the sequences that yield the max profit
    return result

def BuildSolution(Choice, d, c):
    # Backtrack to find the sequences of transactions that lead to the max profit

    if d <= 1: # no profit if there is one day or less
        return []

    if Choice[d-1] == "skip": # if the choice on day d is a skip day, return the choice from the previous day
        return BuildSolution(Choice, d-1, c)

    else:
        stock, buy_day, sell_day = Choice[d-1]

        previous_transactions = BuildSolution(Choice, buy_day - c - 1, c) # pull the sequence of the previous transaction if there is one
        return previous_transactions + [(stock, buy_day, sell_day)] # return the previous sequences if they exist, and add the current transaction to the list
