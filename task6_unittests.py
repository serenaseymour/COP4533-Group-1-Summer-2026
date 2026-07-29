from task6_dp import dp

def tests():

    Example_Problem_3_1 =[
        [2,9,8,4,5,0,7],
        [6,7,3,9,1,0,8],
        [1,7,9,6,4,9,11],
        [7,8,3,1,8,5,2],
        [1,8,4,0,9,2,1]
    ]

    Example_Problem_3_2 =[
        [7,1,5,3,6,8,9],
        [2,4,3,7,9,1,8],
        [5,8,9,1,2,3,10],
        [9,3,4,8,7,4,1],
        [3,1,5,8,9,6,4]
    ]
    
    test_cases = [

        # Problem 3 Examples
        {"name": "Problem 3.1 example", "A": Example_Problem_3_1, "c": 2, "expected": [(3, 1, 3), (2, 6, 7)]},
        {"name": "Problem 3.2 example", "A": Example_Problem_3_2, "c": 2, "expected": [(1, 2, 3), (2, 6, 7)]},

        #No Profit Cases
        {"name": "Empty", "A": [], "c": 1, "expected": []},
        {"name": "Same Prices", "A": [[5, 5, 5, 5]], "c": 1, "expected": []},
        {"name": "All Decreasing", "A": [[10, 8, 7], [5, 4, 3]], "c": 1, "expected": []},
        {"name": "Single Day", "A": [[1], [2], [3]], "c": 1, "expected": []},
        {"name": "One Stock, No Profit", "A": [[5, 4, 3, 2, 1]], "c": 2, "expected": []},
        {"name": "All zeroes", "A": [[0, 0, 0], [0, 0, 0]], "c": 1, "expected": []},

        #Profitable/Increasing Cases
        {"name": "Simple Profit", "A": [[1, 2, 3, 4]], "c": 1, "expected": [(1, 1, 4)]},
        {"name": "Multiple Stocks", "A": [[1, 4], [2, 7]], "c": 1, "expected": [(2, 1, 2)]},
        {"name": "Multiple Transactions, Different Stocks", "A": [[1, 10, 3, 6, 1], [2, 4, 2, 1, 10]], "c": 1, "expected": [(1, 1, 2), (2, 4, 5)]},

        # Cooldown Cases
        {"name": "Large Cooldown", "A": [[1, 10, 1, 8, 9]], "c": 3, "expected": [(1, 1, 2)]},
        {"name": "Multiple Transactions with Cooldown", "A": [[1, 6, 1, 1, 8]], "c": 1, "expected": [(1, 1, 2), (1, 4, 5)]},

    ]

    print("Running Test Cases for Task 6\n ")
    passed = 0
    for idx, tc in enumerate(test_cases, 1): #idx = index, tc = test case
        A = tc["A"]
        m = len(A)
        n = len(A[0]) if m > 0 else 0
        c = tc["c"]

        dynamic = dp(A, m, n, c)

        expected = tc["expected"]
        success = dynamic == expected
        status = "PASS" if success else "FAIL"
        print(f"{idx:2d}. {tc['name']:30} c={c} | Dynamic: {dynamic} |{status}")
        if success:
            passed += 1

    print(f"\nResults: {passed}/{len(test_cases)} tests passed")



if __name__ == "__main__":
    tests()
