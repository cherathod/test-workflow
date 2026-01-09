from src.math_operathion import add, sub

def test_add():
    assert add(1 + 2) == 3
    assert add(0 + 5) == 5

def test_sub():
    assert sub(10 - 20) == -10
    assert sub(5 - 2) == 3