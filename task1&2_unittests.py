from task1_bruteforce import brute_force
from task2_greedy import greedy


def tests():
    test_cases = [
        # Milestone 1 example
        {"name": "Milestone 1 Example", "A": [[12, 1, 5, 3, 16], [4, 4, 13, 4, 9], [6, 8, 6, 1, 2], [14, 3, 4, 8, 10]],
         "expected": (1, 2, 5, 15)},

        # No profit cases
        {"name": "Empty", "A": [], "expected": (0, 0, 0, 0)},
        {"name": "Same Prices", "A": [[5, 5, 5, 5]], "expected": (0, 0, 0, 0)},
        {"name": "All Decreasing", "A": [[10, 8, 7], [5, 4, 3]], "expected": (0, 0, 0, 0)},
        {"name": "Single Day", "A": [[100]], "expected": (0, 0, 0, 0)},
        {"name": "One Stock, No Profit", "A": [[9, 8, 7, 6, 5]], "expected": (0, 0, 0, 0)},

        # Simple increasing cases
        {"name": "Simple Increasing", "A": [[1, 3, 2, 8]], "expected": (1, 1, 4, 7)},
        {"name": "Multiple Peaks", "A": [[7, 1, 5, 3, 6, 4, 10]], "expected": (1, 2, 7, 9)},
        {"name": "Multiple Stocks", "A": [[1, 5], [2, 10], [3, 4]], "expected": (2, 1, 2, 8)},
        {"name": "Best at End", "A": [[10, 1, 2, 3, 4, 5]], "expected": (1, 2, 6, 4)},
        {"name": "Best on Stock 3", "A": [[10, 1], [20, 5], [1, 100]], "expected": (3, 1, 2, 99)},

        # Edge cases
        {"name": "All Zero", "A": [[0, 0, 0]], "expected": (0, 0, 0, 0)},
        {"name": "Negative Profit Only", "A": [[100, 50, 10]], "expected": (0, 0, 0, 0)},
        {"name": "Large Price Difference", "A": [[0, 100000]], "expected": (1, 1, 2, 100000)},
        {"name": "m=1, n=1000", "A": [[i for i in range(100)]], "expected": (1, 1, 100, 99)},
        {"name": "m=50, n=10", "A": [[j * 10 + i for j in range(10)] for i in range(50)], "expected": None},
        {"name": "Random Fluctuations", "A": [[5, 1, 8, 2, 9, 3, 7]], "expected": (1, 2, 5, 8)},
        {"name": "Equal Max Multiple", "A": [[1, 10, 1, 10]], "expected": (1, 1, 2, 9)},
        {"name": "Late Best Buy", "A": [[100, 90, 80, 10, 95]], "expected": (1, 4, 5, 85)},
        {"name": "Single Stock One Peak Early", "A": [[1, 10, 9, 8, 7]], "expected": (1, 1, 2, 9)},
        {"name": "Buy on Last Day Impossible", "A": [[10, 20, 5]], "expected": (1, 1, 2, 10)},
        {"name": "Zero Profit Transaction Only", "A": [[10, 10, 10, 15, 15]], "expected": (1, 1, 4, 5)},
        {"name": "Prices with Duplicates", "A": [[7, 1, 5, 5, 6, 6]], "expected": (1, 2, 5, 5)},
        {"name": "All Stocks Peak on Same Day", "A": [[10, 20], [15, 25], [5, 30]], "expected": (3, 1, 2, 25)},
        {"name": "Minimal Profitable Transaction", "A": [[1, 2]], "expected": (1, 1, 2, 1)},
        {"name": "m=0 Empty Stocks", "A": [], "expected": (0, 0, 0, 0)},
        {"name": "n=2 Minimal Case Profitable", "A": [[50, 100]], "expected": (1, 1, 2, 50)},
        {"name": "n=2 Minimal Case Loss", "A": [[100, 50]], "expected": (0, 0, 0, 0)},
        {"name": "Fluctuating with Multiple Good Options", "A": [[1, 10, 2, 20, 3, 15]], "expected": (1, 1, 4, 19)},
        {"name": "High Volatility Last Stock Best", "A": [[10, 1, 2], [5, 3, 8], [1, 100, 50]],
         "expected": (3, 1, 2, 99)},
    ]

    print("Running Test Cases for Tasks 1 and 2\n")
    passed = 0
    for idx, tc in enumerate(test_cases, 1):
        A = tc["A"]
        m = len(A)
        n = len(A[0]) if m > 0 else 0


        bf = brute_force(A, m, n)
        gr = greedy(A, m, n)


        expected = tc.get("expected")
        success = (bf == expected or expected is None) and bf == gr
        status = "PASS" if success else "FAIL"
        print(f"{idx:2d}. {tc['name']:30} Brute: {bf} | Greedy: {gr} | {status}")
        if success:
            passed += 1


    print(f"\nResults: {passed}/{len(test_cases)} tests passed")





if __name__ == "__main__":
    tests()