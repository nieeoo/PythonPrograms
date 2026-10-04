import importlib

program = importlib.import_module("Code.14_char_frequency")
character_frequency = program.character_frequency

assert character_frequency("hello") == {
    "h": 1, "e": 1, "l": 2, "o": 1
}

assert character_frequency("aaa") == {"a": 3}

print("All test cases passed.")