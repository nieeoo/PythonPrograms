import importlib

program = importlib.import_module("Code.01_check_Even_odd")
Even_Odd = program.Even_Odd

assert Even_Odd(20) == "Even"
assert Even_Odd(11) == "Odd"
assert Even_Odd(0) == "Even"
assert Even_Odd(-5) == "Odd"

print("All test cases passed.")