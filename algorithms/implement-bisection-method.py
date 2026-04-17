"""Compute square roots using the bisection method.

This module demonstrates a simple numeric algorithm for estimating square roots
by repeatedly bisecting an interval and narrowing the search range until the
result is within a chosen tolerance.
"""

def square_root_bisection(number:float | int, tolerance=0.01, max_iterations=100) -> float | None:
    """Estimate the square root of a number using the bisection method.

    Args:
        number (float): The non-negative value to find the square root of.
        tolerance (float): The acceptable error margin for the result.
        max_iterations (int): The maximum number of iterations.

    Returns:
        float | None: The approximate square root if converged, otherwise None.
    """
    # The bisection method only works for non-negative inputs in the real numbers.
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # For 0 and 1, the square root is the same as the number.
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    # Define the initial search interval.
    # If number is between 0 and 1, the square root is larger than the number,
    # so high must be at least 1.0.
    low = 0
    high = max(1.0, number)
    iterations = 0
    root = None

    # Repeat until the interval width is within tolerance or we exhaust iterations.
    while (high - low) > tolerance and iterations < max_iterations:
        mid = (low + high) / 2

        # If mid squared is less than the target, the root lies in the right half.
        if mid**2 < number:
            low = mid
        else:
            # Otherwise, the root lies in the left half or at mid.
            high = mid

        iterations += 1

    # The best estimate is the midpoint of the final interval.
    root = (low + high) / 2.0

    if (high - low) <= tolerance:
        print(f'The square root of {number} is approximately {root}')
        return root
    else:
        print(f'Failed to converge within {max_iterations} iterations')
        return None


if __name__ == "__main__":
    square_root_bisection(2)
    square_root_bisection(0.001, 1e-7, 50)
    square_root_bisection(0.25, 1e-7, 50)
    square_root_bisection(225, 1e-7, 10)
    square_root_bisection(0.001, 1e-7, 50)