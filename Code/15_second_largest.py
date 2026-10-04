def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]


if __name__ == "__main__":
    print(second_largest([10,3,4,2,23,45,67,33,56]))