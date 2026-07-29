# Necessary imports
import random
from task5_dp import dynamic_programming

# Helper function to verify results
def check_solution(A, txns, k):
    # Validates a returned transaction list and totals its profit.
    # Returns (profit, error_message). error_message is "" when the list is legal.
    m = len(A)
    n = len(A[0]) if m > 0 else 0

    limit = max(k, 0)   # A negative k allows nothing, same as k = 0
    if len(txns) > limit:
        return 0, f"used {len(txns)} transactions, limit was {k}"

    profit = 0
    prev_sell = 0
    for (stock, buy, sell) in txns:
        if not (1 <= stock <= m):
            return 0, f"stock {stock} out of range"
        if not (1 <= buy < sell <= n):
            return 0, f"bad day pair ({buy}, {sell})"
        if buy < prev_sell:   # A new buy cannot happen before the previous sell
            return 0, f"transactions overlap at ({buy}, {sell})"
        prev_sell = sell
        profit += A[stock - 1][sell - 1] - A[stock - 1][buy - 1]

    return profit, ""


def tests():
    # Examples from assignments
    EXAMPLE_1 = [[7, 1, 5, 3, 6],
                [2, 9, 3, 7, 9],
                [5, 8, 9, 1, 6],
                [9, 3, 4, 8, 7]]

    EXAMPLE_2 = [[25, 30, 15, 40, 50],
                [10, 20, 30, 25, 5],
                [30, 45, 35, 10, 15],
                [5, 50, 35, 25, 45]]

    test_cases = [
        {"name": "Spec Example k=3 (given)", "A": EXAMPLE_1, "k": 3, "profit": 17},
        {"name": "Spec Example k=1", "A": EXAMPLE_1, "k": 1, "profit": 7},
        {"name": "Spec Example k=2", "A": EXAMPLE_1, "k": 2, "profit": 13},

        {"name": "Problem 2 Example k=1", "A": EXAMPLE_2, "k": 1, "profit": 45},
        {"name": "Problem 2 Example k=2", "A": EXAMPLE_2, "k": 2, "profit": 80},
        {"name": "Problem 2 Example k=3 (given)", "A": EXAMPLE_2, "k": 3, "profit": 90},
        {"name": "Problem 2 Example k=4", "A": EXAMPLE_2, "k": 4, "profit": 100},
        {"name": "Problem 2 Example k=5 Saturates", "A": EXAMPLE_2, "k": 5, "profit": 100},

        # Problem 1 example from Milestone 1, at increasing transaction limits
        {"name": "Problem 1 Example k=1", "A": [[12, 1, 5, 3, 16], [4, 4, 13, 4, 9], [6, 8, 6, 1, 2], [14, 3, 4, 8, 10]],
         "k": 1, "profit": 15},
        {"name": "Problem 1 Example k=2", "A": [[12, 1, 5, 3, 16], [4, 4, 13, 4, 9], [6, 8, 6, 1, 2], [14, 3, 4, 8, 10]],
         "k": 2, "profit": 22},
        {"name": "Problem 1 Example k=3", "A": [[12, 1, 5, 3, 16], [4, 4, 13, 4, 9], [6, 8, 6, 1, 2], [14, 3, 4, 8, 10]],
         "k": 3, "profit": 26},
        {"name": "Problem 1 Example k=4", "A": [[12, 1, 5, 3, 16], [4, 4, 13, 4, 9], [6, 8, 6, 1, 2], [14, 3, 4, 8, 10]],
         "k": 4, "profit": 28},

        # No profit possible, so the answer must be the empty sequence
        {"name": "Empty", "A": [], "k": 3, "profit": 0},
        {"name": "Same Prices", "A": [[5, 5, 5, 5]], "k": 2, "profit": 0},
        {"name": "All Decreasing", "A": [[10, 8, 7], [5, 4, 3]], "k": 2, "profit": 0},
        {"name": "Single Day", "A": [[100]], "k": 3, "profit": 0},
        {"name": "One Stock, No Profit", "A": [[9, 8, 7, 6, 5]], "k": 4, "profit": 0},
        {"name": "All Zero", "A": [[0, 0, 0]], "k": 2, "profit": 0},
        {"name": "Negative Profit Only", "A": [[100, 50, 10]], "k": 3, "profit": 0},

        # k boundary conditions
        {"name": "k=0 On Profitable Grid", "A": [[1, 10, 2, 20]], "k": 0, "profit": 0},
        {"name": "Negative k", "A": [[1, 10]], "k": -1, "profit": 0},
        {"name": "k Larger Than Useful", "A": [[1, 5, 2, 8]], "k": 10, "profit": 10},
        {"name": "k Caps A Better Answer", "A": [[1, 5, 2, 8]], "k": 1, "profit": 7},

        # Single transaction (k=1)
        {"name": "Simple Increasing", "A": [[1, 3, 2, 8]], "k": 1, "profit": 7},
        {"name": "Multiple Peaks", "A": [[7, 1, 5, 3, 6, 4, 10]], "k": 1, "profit": 9},
        {"name": "Multiple Stocks", "A": [[1, 5], [2, 10], [3, 4]], "k": 1, "profit": 8},
        {"name": "Best at End", "A": [[10, 1, 2, 3, 4, 5]], "k": 1, "profit": 4},
        {"name": "Best on Stock 3", "A": [[10, 1], [20, 5], [1, 100]], "k": 1, "profit": 99},
        {"name": "Late Best Buy", "A": [[100, 90, 80, 10, 95]], "k": 1, "profit": 85},
        {"name": "Large Price Difference", "A": [[0, 100000]], "k": 1, "profit": 100000},
        {"name": "Minimal Profitable Transaction", "A": [[1, 2]], "k": 1, "profit": 1},
        {"name": "n=2 Minimal Case Loss", "A": [[100, 50]], "k": 1, "profit": 0},

        # Multiple transactions on one stock
        {"name": "Two Peaks One Stock", "A": [[1, 10, 2, 20, 3, 15]], "k": 2, "profit": 31},
        {"name": "Equal Max Multiple", "A": [[1, 10, 1, 10]], "k": 2, "profit": 18},
        {"name": "Sawtooth k=3", "A": [[1, 5, 1, 5, 1, 5]], "k": 3, "profit": 12},
        {"name": "Sawtooth Limited to k=2", "A": [[1, 5, 1, 5, 1, 5]], "k": 2, "profit": 8},
        {"name": "Random Fluctuations", "A": [[5, 1, 8, 2, 9, 3, 7]], "k": 3, "profit": 18},

        # Transactions that must switch between stocks
        {"name": "Switch Stocks Between Trades", "A": [[1, 9, 9, 9], [5, 5, 1, 12]], "k": 2, "profit": 19},
        {"name": "Sell And Buy Same Day", "A": [[1, 10, 10], [5, 5, 30]], "k": 2, "profit": 34},
        {"name": "High Volatility Last Stock Best", "A": [[10, 1, 2], [5, 3, 8], [1, 100, 50]], "k": 2, "profit": 104},
        {"name": "Three Stocks Three Trades", "A": [[1, 6, 2, 2], [3, 3, 1, 9], [4, 4, 4, 4]], "k": 3, "profit": 13},

        # Larger inputs
        {"name": "m=1, n=100 Increasing", "A": [[i for i in range(100)]], "k": 1, "profit": 99},
        {"name": "m=50, n=10", "A": [[j * 10 + i for j in range(10)] for i in range(50)], "k": 2, "profit": 90},
    ]

    print("Running Test Cases for Task 5\n")
    passed = 0
    for idx, tc in enumerate(test_cases, 1):
        A = tc["A"]
        m = len(A)
        n = len(A[0]) if m > 0 else 0
        k = tc["k"]

        dp = dynamic_programming(A, m, n, k)

        # A returned sequence has to be legal, and its profit has to be optimal
        profit, error = check_solution(A, dp, k)
        expected = tc["profit"]
        success = (error == "" and profit == expected)
        status = "PASS" if success else "FAIL"

        detail = error if error else f"profit {profit}, expected {expected}"
        print(f"{idx:2d}. {tc['name']:32} k={k:<3} {str(dp):28}\n\t{detail:34} {status}")
        if success:
            passed += 1

    print(f"\nResults: {passed}/{len(test_cases)} tests passed")
    return passed == len(test_cases)

# Main logic for test units
if __name__ == "__main__":
    tests_sets = tests()
    print()

    print("\nALL TESTS PASSED" if (tests_sets) else "\nSOME TESTS FAILED")
