import importlib

program = importlib.import_module("Code.10_sum_of_digits")
sum_of_digits = program.sum_of_digits

assert sum_of_digits(12345) == 15
assert sum_of_digits(908) == 17
assert sum_of_digits(100) == 1
assert sum_of_digits(0) == 0

print("All test cases passed.")