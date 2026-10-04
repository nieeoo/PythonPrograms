import importlib

program = importlib.import_module("Code.20_word_frequency")
word_frequency = program.word_frequency

assert word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert word_frequency("python python code") == {
    "python": 2,
    "code": 1
}

print("All test cases passed.")