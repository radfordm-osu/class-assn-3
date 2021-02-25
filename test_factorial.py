import fibonacci

def test_factorial_word():
    assert fibonacci.Factorial("hi") == -1

def test_factorial_zero():
    assert fibonacci.Factorial(0) == -1

def test_factorial_num():
    assert fibonacci.Factorial(6) == 720
