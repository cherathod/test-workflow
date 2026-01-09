from src.math_operathion import add, sub, div

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(10, 20) == -10

def test_div():
    assert div(20, 2) == 10