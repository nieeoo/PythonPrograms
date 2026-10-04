import importlib

program = importlib.import_module("Code.15_second_largest")
second_largest = program.second_largest

assert second_largest([10, 5, 8, 20, 15]) == 15
assert second_largest([1, 2, 3]) == 2
assert second_largest([10, 20, 30, 40]) == 30

print("All test cases passed.")