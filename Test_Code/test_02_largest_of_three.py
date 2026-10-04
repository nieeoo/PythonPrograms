import importlib

program = importlib.import_module("Code.02_largest_of_three_numbers")
largest_of_three = program.largest_of_three

assert largest_of_three(10, 20, 30) == 30
assert largest_of_three(50, 20, 10) == 50
assert largest_of_three(5, 5, 2) == 5
assert largest_of_three(-1, -5, -3) == -1

print("All test cases passed.")