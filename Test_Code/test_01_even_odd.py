from Code.01_check_Even_odd
import Even_Odd # pyright: ignore[reportUndefinedVariable]

def test_even_number():
    assert Even_Odd(10) == "Even"

def test_odd_number():
    assert Even_Odd(7) == "Odd"

def test_zero():
    assert Even_Odd(0) == "Even"

def test_negative_even():
    assert Even_Odd(-4) == "Even"

def test_negative_odd():
    assert Even_Odd(-5) == "Odd"