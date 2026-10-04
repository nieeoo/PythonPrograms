def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

if __name__ == "__main__":
    print(reverse_number(2345167))
    print(reverse_number(23432))