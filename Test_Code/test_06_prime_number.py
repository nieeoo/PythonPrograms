import importlib

program = importlib.import_module("Code.06_prime_number")
is_prime = program.is_prime

assert is_prime(17) == True
assert is_prime(10) == False
assert is_prime(2) == True
assert is_prime(1) == False

print("All test cases passed.")