def is_palindrome_string(text):
    return text == text[::-1]


if __name__ == "__main__":
    print(is_palindrome_string("pop"))
    print(is_palindrome_string("hello"))