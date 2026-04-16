"""Algorithms notes for binary search and merge sort.

This module contains simple implementations of the binary search and merge sort
algorithms with example usage.
"""

def binary_search(arr, target):
    """Perform binary search on a sorted list.

    Args:
        arr (list): A sorted list of comparable items.
        target: The item to search for.

    Returns:
        int: The index of target in arr if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def merge_sort(arr):
    """Sort a list using the merge sort algorithm.

    Args:
        arr (list): The list of comparable items to sort.

    Returns:
        list: A new list containing the sorted items.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


if __name__ == "__main__":
    # Example usage for binary search
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(arr, target)
    print(f"Element found at index: {result}")

    # Example usage for merge sort
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")