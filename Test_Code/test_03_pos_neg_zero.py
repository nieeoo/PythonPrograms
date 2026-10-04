import importlib

program = importlib.import_module("Code.03_pos_neg_zero")
check_number = program.check_number

assert check_number(10) == "Number is Positive"
assert check_number(-5) == "Number is Negative"
assert check_number(0) == "Number is Zero"

print("All test cases passed.")