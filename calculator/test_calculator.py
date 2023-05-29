import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_addition2(self):
        assert 5 == calculator.add(2, 3)

    def test_addition3(self):
        assert 1 == calculator.add(-2, 3)
