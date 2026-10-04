def sum_of_digits(num):
    total = 0

    while num> 0:
        total += num % 10
        num //= 10

    return total

if __name__ == "__main__":
    print(sum_of_digits(12367))
    print(sum_of_digits(342))