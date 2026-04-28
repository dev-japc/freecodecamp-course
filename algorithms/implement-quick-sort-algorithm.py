def quick_sort(int_list :list):
    """
    Sorts a list of integers using the quick sort algorithm and returns a new sorted list.

    Quick sort is a divide-and-conquer algorithm that:
    1. Selects a 'pivot' element from the list (here, the last element).
    2. Partitions the other elements into sublists of elements less than, equal to, and greater than the pivot.
    3. Recursively sorts the sublists and combines them with the pivot(s).

    Args:
        int_list (list): The list of integers to be sorted.

    Returns:
        list: A new sorted list of integers.
    """
    # Handle the case where the input list is empty
    if not int_list:
        return []  # Return an empty list if input is empty

    # Base case: if the list has one or zero elements, it is already sorted
    if len(int_list) <= 1:
        return int_list

    # Choose the last element as the pivot
    pivot = int_list[-1]

    # Partition the list into elements less than, equal to, and greater than the pivot
    left = [elem for elem in int_list if elem < pivot]    # Elements less than pivot
    right = [elem for elem in int_list if elem > pivot]   # Elements greater than pivot
    middle = [elem for elem in int_list if elem == pivot] # Elements equal to pivot
    
    # Recursively sort the left and right sublists, then concatenate the results
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    # Example usage: sort a sample list and print the result
    print(quick_sort([20, 3, 14, 1, 5]))