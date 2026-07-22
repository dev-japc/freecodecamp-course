"""Generate balanced parentheses pairs using breadth-first search.

This module defines :func:`gen_parentheses`, which constructs all valid
balanced parentheses strings for a given number of pairs. It uses a queue to
expand partial sequences in BFS order, ensuring that only valid openings and
closings are enqueued.

Example:
    >>> gen_parentheses(2)
    ['(())', '()()']
"""


def gen_parentheses(pairs):
    """Generate all balanced parentheses combinations.

    Args:
        pairs (int): The number of pairs of parentheses to generate.

    Returns:
        list[str] | str: A list of valid balanced parentheses strings when the
        input is valid, otherwise an error message string.
    """

    # If the input is not an integer, return a helpful message.
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'

    # If the input is less than 1, return a helpful message.
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    
    # The queue stores tuples of the form:
    # (current_string, opens_used, closes_used)
    # Start with an empty string and zero parentheses used.
    queue = [('', 0, 0)]

    # The list to collect complete balanced sequences.
    result = []

    # Continue until there are no more partial sequences to process.
    while queue:
        current, opens_used, closes_used = queue.pop(0)

        # If the current string has reached the final length, it is complete.
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            # Add an opening parenthesis if we still have opens remaining.
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))

            # Add a closing parenthesis if it does not lead to imbalance.
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    
    return result


if __name__ == '__main__':
    # Example calls for when this module is executed directly.
    print(gen_parentheses(2))
    print(gen_parentheses(3))