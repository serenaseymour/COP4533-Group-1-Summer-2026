def dynamic(A, m, n):
    # Task 3: Dynamic Solution for Problem 1
    
    # Step 1 is to create our 2-dimensional M array and fill it with infinite placeholder values
    M = [[float('inf') for _ in range(n)] for _ in range(m)]

    # For step 2, we do our dynamic tabulation, processing M for each possible [i,j] index in the [m,n] matrix
    for i in range(m):
        # 1 to n since it's not possible to sell on the first day anyway.
        for j in range(1, n):
            # This first if statement was the sole logical change to this algorithm from milestone 2.
            # It bypasses the indexOutOfBounds error that would occur were we to try and access index infinity.
            # Logically however, it changes nothing since the left side A[i][j-1] would always have been less than
            # infinity anyway.
            if M[i][j-1] == float('inf'):
                M[i][j] = j-1
            elif A[i][j-1] < A[i][M[i][j-1]]:
                M[i][j] = j-1
            else:
                M[i][j] = M[i][j-1]

    # Finally step 3, where we follow a similar path to the brute force solution
    # yet rely on our previously solved sub-problem solutions stashed in M
    temp_max = 0
    for i in range(m):
        for j in range(1, n):
            daily_max_profit = A[i][j]-A[i][M[i][j]]
            if daily_max_profit > temp_max:
                temp_max = daily_max_profit
                temp_buy = M[i][j]
                temp_sell = j
                temp_stock = i
    if temp_max <= 0:
        return (0, 0, 0, 0)
    else:
        return (temp_stock+1, temp_buy+1, temp_sell+1, temp_max)