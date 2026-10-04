import importlib

program = importlib.import_module("Code.18_missing_number")
missing_number = program.missing_number

assert missing_number([1, 2, 3, 5]) == 4
assert missing_number([1, 2, 3, 4, 6]) == 5
assert missing_number([1]) == 2

print("All test cases passed.")