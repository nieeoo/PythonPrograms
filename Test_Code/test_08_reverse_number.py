import importlib

program = importlib.import_module("Code.08_reverse_number")
reverse_number = program.reverse_number

assert reverse_number(12345) == 54321
assert reverse_number(908) == 809
assert reverse_number(100) == 1

print("All test cases passed.")