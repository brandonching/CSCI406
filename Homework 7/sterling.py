def stirling(n, k):
    # Base case 1 & 4
    if (k == 0 and n > 0) or (n < k):
        return 0
    # Base case 2 & 3
    elif (n == k and k >= 0) or (k == 1 and n > 1):
        return 1
    # General Case
    else:
        return (k * stirling(n-1, k)) + stirling(n-1, k-1)


def sterling_top_down(n, k):
    # Create a dictionary to store the results
    S = {}
    # Base case 1 & 4
    if (k == 0 and n > 0) or (n < k):
        return 0
    # Base case 2 & 3
    elif (n == k and k >= 0) or (k == 1 and n > 1):
        return 1
    # General Case
    else:
        if (n, k) not in S:
            S[(n, k)] = (k * sterling_top_down(n-1, k)) + \
                sterling_top_down(n-1, k-1)
        return S[(n, k)]


def stirling_bottom_up(n, k):
    # Create a 2D array to store the results
    S = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for row in range(n+1):
        # Base cases
        if k >= 1 and row > 1:
            S[row][1] = 1
        if k >= row:
            S[row][row] = 1

        # General Case
        if row >= 3 and k >= 2:
            for col in range(2, min(row, k)+1):
                S[row][col] = (col * S[row-1][col]) + S[row-1][col-1]

    return S[n][k]


if __name__ == "__main__":
    for n in range(0, 8):
        for k in range(0, 8):
            print(stirling_bottom_up(n, k), end=" ")
        print()
