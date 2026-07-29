# Necessary imports
from collections import namedtuple

# Two record types stored in the Choice table, one per kind of decision
Skip = namedtuple("Skip", ["type", "t", "day"])                       # carry yesterday's profit forward
Sell = namedtuple("Sell", ["type", "stock", "buy_day", "sell_day"])   # a transaction ends on this day

# Returns a list of (stock, buy_day, sell_day)
def dynamic_programming(A, m, n, k):
    # A is an array of size m * n (m rows (stocks), n columns (days))
    # k is maximum number of transactions allowed

    if n < 2 or k <= 0:   # Fewer than 2 days or no transactions allowed, so no
        return []         # profitable buy-sell transaction can be made

    # DP[t][d] = maximum profit using at most t transactions over days 1 through d
    # Choice[t][d] = the decision that produced DP[t][d], used to rebuild the answer
    # Column 0 of each row is unused so the tables can be indexed by day directly
    DP = [[0] * (n + 1) for _ in range(k + 1)]
    Choice = [[None] * (n + 1) for _ in range(k + 1)]

    for d in range(1, n + 1):   # Base case: with 0 transactions, profit is always 0
        DP[0][d] = 0
        Choice[0][d] = None

    for t in range(1, k + 1):   # Base case: on day 1 we cannot sell yet, so profit is 0
        DP[t][1] = 0
        Choice[t][1] = None

    for t in range(1, k + 1):   # Try using up to t transactions
        best_buy_profit = [0] * (m + 1)
        best_buy_day = [1] * (m + 1)

        for i in range(1, m + 1):   # Start by assuming stock i is bought on day 1
            best_buy_profit[i] = DP[t - 1][1] - A[i - 1][0]
            best_buy_day[i] = 1

        for d in range(2, n + 1):   # Scan days from left to right
            DP[t][d] = DP[t][d - 1]
            Choice[t][d] = Skip("skip", t, d - 1)

            for i in range(1, m + 1):   # Try selling each stock on day d
                current_profit = best_buy_profit[i] + A[i - 1][d - 1]
                if current_profit > DP[t][d]:   # Selling stock i today is better, so
                    DP[t][d] = current_profit   # remember the stock, buy day, and sell day
                    Choice[t][d] = Sell("sell", i, best_buy_day[i], d)

            for i in range(1, m + 1):   # Update the best buy option for future days
                possible_buy_profit = DP[t - 1][d] - A[i - 1][d - 1]
                if possible_buy_profit > best_buy_profit[i]:   # Buying today gives a better
                    best_buy_profit[i] = possible_buy_profit   # future opportunity, so update
                    best_buy_day[i] = d                        # the best buy day for this stock

    if DP[k][n] <= 0:   # No positive profit is possible, so make no trades
        return []

    return build_solution(Choice, k, n)


# Walks the Choice table backwards from cell [t][d] to rebuild the solution
def build_solution(Choice, t, d):
    if t == 0:   # No transactions left
        return []

    # Step back over days that end in no transaction
    while d > 1 and Choice[t][d] is not None and Choice[t][d].type == "skip":
        d -= 1

    if d <= 1 or Choice[t][d] is None:   # No possible sell day, or nothing recorded
        return []

    stock = Choice[t][d].stock
    buy_day = Choice[t][d].buy_day
    sell_day = Choice[t][d].sell_day

    # This transaction buys on buy_day, so any earlier transactions must
    # finish on or before buy_day to matche the non-overlapping rule
    previous_transactions = build_solution(Choice, t - 1, buy_day)
    return previous_transactions + [(stock, buy_day, sell_day)]
