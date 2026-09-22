def find_factorial(number):
    if number == 0:
        return 1
    else:
        return number + find_factorial(number - 1)

if __name__ == "__main__":
    print(find_factorial(5))
    print(find_factorial(0))