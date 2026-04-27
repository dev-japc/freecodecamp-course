def merge_sort(array):
    """
    Sorts an array in place using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm that recursively splits the array into halves,
    sorts each half, and then merges the sorted halves back together.

    Args:
        array (list): The list of elements to be sorted. Sorting is done in place.
    """
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(array) <= 1:
        return

    # Find the middle point to divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]   # Left half
    right_part = array[middle_point:]  # Right half

    # Recursively sort both halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Indices for traversing the left, right, and merged array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the sorted halves back into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Compare elements from both halves and copy the smaller one
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from the left half (if any)
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from the right half (if any)
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Example usage
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)