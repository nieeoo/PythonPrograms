import importlib

program = importlib.import_module("Code.09_palindrome_number")
is_palindrome = program.is_palindrome

assert is_palindrome(121) == True
assert is_palindrome(123) == False
assert is_palindrome(1221) == True

print("All test cases passed.")