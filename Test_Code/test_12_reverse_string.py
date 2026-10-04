import importlib

program = importlib.import_module("Code.12_reverse_string")
reverse_string = program.reverse_string

assert reverse_string("Hello") == "olleH"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("abc") == "cba"

print("All test cases passed.")