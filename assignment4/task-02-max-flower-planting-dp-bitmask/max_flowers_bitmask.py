def is_valid(state, m):
    # Check horizontal adjacency
    for i in range(1, m):
        if (state & (1 << i)) and (state & (1 << (i - 1))):
            return False
    return True

def max_flowers(grid, n, m):
    # Edge case: Handle empty grid
    if n == 0 or m == 0:
        return 0

    # Initialize dp table
    dp = [[-1] * (1 << m) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: zero flowers at the start

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1 << m):
            if not is_valid(j, m):
                continue
            for k in range(1 << m):
                if dp[i - 1][k] == -1:
                    continue
                valid = True
                for l in range(m):
                    # Check for valid grid characters
                    if grid[i - 1][l] not in '01':
                        raise ValueError("Grid must only contain '0' and '1'")
                    if (j & (1 << l)) and grid[i - 1][l] == '0':
                        valid = False  # Can't plant flowers in '0' plots
                    if (j & (1 << l)) and (k & (1 << l)):
                        valid = False  # Can't plant flowers in adjacent plots
                    if (j & (1 << l)) and (l > 0) and (k & (1 << (l - 1))):
                        valid = False  # Can't plant flowers in left adjacent
                    if (j & (1 << l)) and (l < m - 1) and (k & (1 << (l + 1))):
                        valid = False  # Can't plant flowers in right adjacent
                if valid:
                    count = bin(j).count('1')
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + count)

    # Check for the maximum number of flowers planted
    return max(dp[n]) if dp[n] else 0

# Test cases
def test():
    test_cases = [
        (['010', '101', '010'], 3, 3),
        (['111', '000', '111'], 3, 3),
        (['0110', '1010', '0110'], 3, 4),
        (['0', '1', '0', '1'], 4, 1),
        ([''], 0, 0)
    ]
    
    for i, (grid, n, m) in enumerate(test_cases):
        print(f"Test case {i+1}: grid={grid}, n={n}, m={m} -> Max flowers: {max_flowers(grid, n, m)}")

test()
