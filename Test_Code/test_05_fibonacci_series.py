import importlib

program = importlib.import_module("Code.05_fibonacci_series")
fibonacci = program.fibonacci

assert fibonacci(5) == [0, 1, 1, 2, 3]
assert fibonacci(1) == [0]
assert fibonacci(3) == [0, 1, 1]

print("All test cases passed.")
