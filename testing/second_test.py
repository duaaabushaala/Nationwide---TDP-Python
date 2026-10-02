def add(a,b):
    return a*b

def test_add():
    result = add(2,2)
    assert result == 4

def add1():
    result = add(10, 20)
    assert result == 30