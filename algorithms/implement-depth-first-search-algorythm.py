'''
Depth-First Search (DFS) example using an adjacency matrix.

This script shows how to traverse a graph by visiting a node, then
recursively exploring each unvisited neighbor before backtracking.
The expected output for the first example is a traversal order that
includes 1, 2, 3, and 0.
'''


def dfs(adj_matrix, start_node):
    """
    Perform a depth-first traversal of a graph represented by an adjacency matrix.

    Args:
        adj_matrix: A 2D list where adj_matrix[u][v] == 1 means there is an edge
            from node u to node v.
        start_node: The index of the node where traversal begins.

    Returns:
        The traversal order printed to the console.
    """
    n = len(adj_matrix)
    visited = [False] * n
    traversal_order = []

    def traverse(node):
        # Mark the current node as visited and record it in the traversal order.
        visited[node] = True
        traversal_order.append(node)

        # Explore each possible neighbor and continue recursively.
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                traverse(neighbor)

    traverse(start_node)
    return print(traversal_order)


if __name__ == '__main__':
    # Example 1: a simple connected path that should produce [1, 2, 3, 0].
    dfs([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
    ], 1)

    # Example 2: a graph that branches from node 0.
    dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0)

    # Example 3: traversal starting from the last node.
    dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3)