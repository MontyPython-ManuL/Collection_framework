import unittest
from anagrams.func_reverse import rev_text


class TestStringReverse(unittest.TestCase):
    def test_typical_string_symbol(self):
        cases_typical = [('O@leh rymy3doloV h2appy', 'h@elO Volo3dymyr y2ppah'),
                         ('O!!!leh rymy???doloV', 'h!!!elO Volo???dymyr'),
                         ('O!!#leh', 'h!!#elO'),
                         ('O!!#leh rymy3doloV h2appy', 'h!!#elO Volo3dymyr y2ppah')]

        for text, result_text in cases_typical:
            self.assertEqual(rev_text(text), result_text)

    def test_atypical_only_symbol(self):
        cases_atypical = [('', ''),
                          ('12345', '12345'),
                          ('1*$#2345', '1*$#2345'),
                          ('123124135256346457586897978089-9-90-',
                           '123124135256346457586897978089-9-90-')]
        for text, result_text in cases_atypical:
            self.assertEqual(rev_text(text), result_text)


if __name__ == '__main__':
    unittest.main()
