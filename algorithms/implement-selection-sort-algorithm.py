def selection_sort(array: list) -> list:

    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate over each element in the array by its index and value
    for selection_index, selection in enumerate(array):
        # Assume the current position holds the minimum value
        minimum_index = selection_index
        minimum_value = selection

        # Iterate over the unsorted portion of the array
        for index in range(selection_index, len(array)):
            # If a smaller value is found, update minimum_index and minimum_value
            if array[index] < minimum_value:
                minimum_index = index
                minimum_value = array[index]
                # Swap the found minimum value with the value at the current selection_index
                array[minimum_index], array[selection_index] = array[selection_index], array[minimum_index]

    # Return the sorted array
    return array


# Example usage and test cases
if __name__ == '__main__':
    # Test with a small list
    print(selection_sort([33, 1, 89, 2, 67, 245]))
    # Test with a larger list
    print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))