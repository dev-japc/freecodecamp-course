def countup(number):
    if number < 1:
        return []
    count_list = countup(number - 1)
    count_list.append(number)
    return count_list

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    try:
        if number < 1:
            raise ValueError("Number must be greater than 0")
    except ValueError as e:
        print(e)
        exit(1)
        
    result = countup(number)
    if result is not None:
        print(result)
    else:
        print("No numbers to count up.")