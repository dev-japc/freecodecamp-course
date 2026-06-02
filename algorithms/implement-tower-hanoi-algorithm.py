"""Tower of Hanoi solver with complete line-by-line documentation.

This module defines `hanoi_solver` to compute the sequence of rod states
for the Tower of Hanoi problem. Each line of the returned string shows the
current contents of the three rods at one step in the solution.
"""


def hanoi_solver(disks: int) -> str:
    """Return the Tower of Hanoi solution trace for a given number of disks.

    Parameters
    ----------
    disks : int
        The number of disks to move from the first rod to the third rod.
        Must be a non-negative integer.

    Returns
    -------
    str
        The step-by-step state of the three rods as a newline-separated string.
        If the input is invalid, returns an error message string.
    """

    # Attempt to convert the input to an integer in case a numeric string is passed.
    try:
        disks = int(disks)
        # If the integer is negative, consider that invalid input.
        if disks < 0:
            raise ValueError("The number of disks should be positive")
    except (ValueError, TypeError):
        # Return a friendly error message for invalid inputs.
        return f"Error: The number of disks should be positive | your input:{disks}"

    # Build the first rod with disks ordered from largest to smallest.
    # The list stores disks as integers; larger integers mean larger disks.
    rod_1 = [x for x in range(disks, 0, -1)]
    # The two other rods start empty.
    rod_2 = []
    rod_3 = []

    # `steps` will collect the state of the rods after each move.
    steps = []

    def get_state():
        # Return the current state of all rods as a single formatted string.
        # This function reads the three lists and formats them with spaces.
        return f"{rod_1} {rod_2} {rod_3}"

    def move(n, start, auxiliary, end):
        # Recursively move `n` disks from `start` rod to `end` rod.
        if n == 1:
            # Base case: move one disk directly from start to end.
            end.append(start.pop())
            # Record the rods' state after the move.
            steps.append(get_state())
        else:
            # Step 1: move n-1 disks from start to auxiliary rod.
            move(n - 1, start, end, auxiliary)
            # Step 2: move the remaining disk from start to end.
            end.append(start.pop())
            # Record the order after moving the largest disk.
            steps.append(get_state())
            # Step 3: move the n-1 disks from auxiliary to end.
            move(n - 1, auxiliary, start, end)

    # Add the initial state before any moves happen.
    steps.append(get_state())

    if disks > 0:
        # Trigger the recursive algorithm if there is at least one disk.
        move(disks, rod_1, rod_2, rod_3)

    # Join all recorded steps into a single string with newline separators.
    return "\n".join(steps)


if __name__ == "__main__":
    # Print a small example trace when the script is executed directly.
    print(hanoi_solver(-2))