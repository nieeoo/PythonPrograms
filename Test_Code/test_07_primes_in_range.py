import importlib

program = importlib.import_module("Code.07_primes_in_range")
primes_in_range = program.primes_in_range

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]

print("All test cases passed.")