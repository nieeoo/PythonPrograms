import importlib

program = importlib.import_module("Code.19_find_duplicates")
find_duplicates = program.find_duplicates

assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]
assert find_duplicates([1, 2, 3]) == []

print("All test cases passed.")