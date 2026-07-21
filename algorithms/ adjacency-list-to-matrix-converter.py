"""adjacency-list-to-matrix-converter

This module provides a small utility to convert a graph represented as
an adjacency list (a dict mapping each node to a list of its neighbours)
into an adjacency matrix (a list of lists where entry [i][j] is 1 when
there is an edge from node i to node j, otherwise 0).

Example adjacency list:

    {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [2]
    }

The corresponding adjacency matrix (printed row by row) is:

    [0, 1, 1, 0]
    [0, 0, 1, 0]
    [1, 0, 0, 1]
    [0, 0, 1, 0]

The module exposes the function :func:`adjacency_list_to_matrix` and a
small example under the usual ``if __name__ == '__main__'`` guard.
"""

def adjacency_list_to_matrix(adj_list: dict):
    """Convert an adjacency list to an adjacency matrix.

    Args:
        adj_list (dict): Mapping from node index (int) to list of neighbour
            indices (ints). Nodes are expected to be 0..n-1 but the function
            works with any set of integer keys that form a contiguous range.

    Returns:
        list[list[int]]: The adjacency matrix as a list of rows (each row is
        a list of ints 0/1).
    """

    # Create an empty list which will become the adjacency matrix.
    adj_matrix = []

    # For each node in the adjacency list, create a row of zeros.
    # We use a separate loop to build the empty matrix with the correct
    # dimensions: one row per node and one column per node.
    for node in adj_list.keys():
        # Append a new row of zeros. The inner comprehension iterates over the
        # keys again to ensure the row length matches the number of nodes.
        adj_matrix.append([0 for _ in adj_list.keys()])

    # Populate the matrix: for each node and its neighbours, set the cell
    # at (node, neighbour) to 1 to indicate a directed edge from node ->
    # neighbour.
    for node, neighbours in adj_list.items():
        for neighbour in neighbours:
            # Set the corresponding matrix cell to 1.
            adj_matrix[node][neighbour] = 1

    # Print each row of the adjacency matrix to provide a visual output.
    for row in adj_matrix:
        print(row)

    # Return the completed adjacency matrix for programmatic use.
    return adj_matrix


if __name__ == '__main__':
    # Example usage guarded by __main__ so it doesn't run on import.
    example = {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}
    adjacency_list_to_matrix(example)