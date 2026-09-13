def dfs_n_queens(n: int):
    solutions = []
    visited = []
    
    # Requirement: Return empty list if n < 1
    if n < 1:
        return []

    def dive_in(matrix_size, row):
        # Base case: All queens placed
        if row >= matrix_size:
            solutions.append(visited.copy())
            return

        for col in range(matrix_size):
            # Check column conflict and diagonal conflicts
            if col not in visited and all(abs(col - v) != abs(row - i) for i, v in enumerate(visited)):
                visited.append(col)
                dive_in(matrix_size, row + 1)
                visited.pop()  # Backtrack

    dive_in(n, 0)

    # Return the actual list of solutions
    return solutions


if __name__ == '__main__':
    print(f"n = 1: {dfs_n_queens(1)}")
    # Expected: [[0]]

    print(f"n = 2: {dfs_n_queens(2)}")
    # Expected: []

    print(f"n = 4: {dfs_n_queens(4)}")
    # Expected: [[1, 3, 0, 2], [2, 0, 3, 1]]