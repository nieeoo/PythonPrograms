def is_palindrome(num):
    return str(num) == str(num)[::-1]


if __name__=="__main__":
    print(is_palindrome(232))
    print(is_palindrome(123))