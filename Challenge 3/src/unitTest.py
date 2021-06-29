import unittest
import find_value as fv

class TestFv(unittest.TestCase):

    def test_fv(self):
        self.assertEqual(fv({'a':{'b':{'c':6}}},'c'), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(fv({'x':{'y':{'z':6}}},'z'), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
