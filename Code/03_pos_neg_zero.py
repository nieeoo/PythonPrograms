def check_number(num):
    if num > 0:
        return "Number is Positive"
    elif num < 0:
        return "Number is Negative"
    else:
        return "Number is Zero"


if __name__ == "__main__":
    print(check_number(10))
    print(check_number(-5))
    print(check_number(0))