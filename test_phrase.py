class TestPhrase:

    def test_chek_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f'{phrase} more 15 simb'