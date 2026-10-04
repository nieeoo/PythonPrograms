import importlib

program = importlib.import_module("Code.11_vowels_consonants")
count_vowels_consonants = program.count_vowels_consonants

assert count_vowels_consonants("Hello World") == (3, 7)
assert count_vowels_consonants("Python") == (1, 5)
assert count_vowels_consonants("aeiou") == (5, 0)

print("All test cases passed.")