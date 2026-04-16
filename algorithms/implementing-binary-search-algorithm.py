"""Binary search implementation with path tracking.

This module provides a binary search function that records the values
inspected along the search path and returns either the path plus a success
message or an empty path with a not-found message.
"""

def binary_search(search_list, value):
    """Search for a value in a sorted list using binary search.

    Args:
        search_list (list): A sorted list of comparable values.
        value: The value to search for in the list.

    Returns:
        tuple[list, str]: A tuple containing the search path and a result message.
    """
    # Track the values examined during the search for demonstration purposes.
    path_to_target = []

    # Initialize the search bounds for the sorted list.
    low = 0
    high = len(search_list) - 1

    # Continue until the search range is exhausted.
    while low <= high:
        # Use integer division to find the middle index.
        mid = (low + high) // 2
        value_at_middle = search_list[mid]

        # Record the inspected value for later explanation.
        path_to_target.append(value_at_middle)

        # If the middle value is the target, return the path and index.
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'

        # If the target is larger than the middle value,
        # narrow search to the right half.
        elif value > value_at_middle:
            low = mid + 1

        # Otherwise, narrow search to the left half.
        else:
            high = mid - 1

    # If we exit the loop, the value was not found.
    return [], "Value not found"


if __name__ == "__main__":
    # Example searches to show how the algorithm behaves.
    print(binary_search([1, 2, 3, 4, 5], 3))
    print(binary_search([1, 2, 3, 4, 5, 9], 4))
    print(binary_search([1, 3, 5, 9, 14, 22], 10))