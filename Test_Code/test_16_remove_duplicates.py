import importlib

program = importlib.import_module("Code.16_remove_duplicates")
remove_duplicates = program.remove_duplicates

assert remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
assert remove_duplicates([1, 1, 1]) == [1]

print("All test cases passed.")