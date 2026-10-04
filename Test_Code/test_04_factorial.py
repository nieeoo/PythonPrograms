import importlib

program = importlib.import_module("Code.04_factorial")
factorial = program.factorial

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(3) == 6

print("All test cases passed.")