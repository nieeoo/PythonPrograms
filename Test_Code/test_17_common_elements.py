import importlib

program = importlib.import_module("Code.17_common_elements")
common_elements = program.common_elements

assert set(common_elements([1, 2, 3], [2, 3, 4])) == {2, 3}
assert set(common_elements([1, 2], [3, 4])) == set()

print("All test cases passed.")