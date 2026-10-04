import importlib

program = importlib.import_module("Code.13_palindrome_string")
is_palindrome_string = program.is_palindrome_string

assert is_palindrome_string("madam") == True
assert is_palindrome_string("hello") == False
assert is_palindrome_string("level") == True

print("All test cases passed.")