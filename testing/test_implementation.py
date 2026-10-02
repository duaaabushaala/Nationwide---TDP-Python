from implementation import tax_calculator


def test_tax_less_than_1000():
    assert tax_calculator(500) == 0


def test_tax_at_1000():
    assert tax_calculator(1000) == 100


def test_tax_between_1000_and_2000():
    assert tax_calculator(1500) == 150


def test_tax_at_2000():
    assert tax_calculator(2000) == 200


def test_tax_greater_than_2000():
    assert tax_calculator(2500) == 500