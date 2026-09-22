def fibonacci(n):
    sequence = [0, 1]

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    number = n + 1
    for item in range(number):
        x = sequence[item] + sequence[item + 1]
        sequence.append(x)
        # print(sequence)

    return sequence[n]
    '''Your fibonacci function is returning the entire result list instead of 
    the single Fibonacci number for the given n. Update the loop to correctly 
    compute each new Fibonacci value, store it in sequence, and return sequence[n] 
    (the nth element) rather than the full list, and try again.
    '''

print(fibonacci(10))