def range_of_numbers(start_num, end_num):
    if start_num < 1:
        return []

    if start_num == end_num:
        return [start_num]
    
    result = range_of_numbers(start_num, end_num -1)
    result.append(end_num)
    
    return result

if __name__ == "__main__":
    print(range_of_numbers(1, 5))
    print(range_of_numbers(5, 5))
