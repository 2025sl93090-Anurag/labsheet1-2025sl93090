import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    print("add function passed")

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    print("subtract function passed")

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    print("multiply function passed")

def test_divide():
    assert calculator.divide(10, 2) == 5.0
    print("divide function passed")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
