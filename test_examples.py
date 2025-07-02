class TestExample:
    def test_chek_math(self):
        a = 5
        b = 9
        assert a+b == 14

    def test_chek_math2(self):
        a = 5
        b = 9
        expected_sum = 12
        assert a+b == expected_sum, f'error report {expected_sum}'