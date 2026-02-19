def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    
    pattern = []
    for i in range(1, n+1):
        pattern.append(str(i))
    
    result = ' '.join(pattern)
    print(result)
    return result
x = number_pattern(4)
