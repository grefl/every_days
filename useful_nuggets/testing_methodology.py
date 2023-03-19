import unittest


def some_libary_function():
    return None
if __name__ == '__main__':
    class TestMe(unittest.TestCase):
        def test_1(self):
            print('I only run when you call this file as python [filename].py')
            self.assertTrue(some_libary_function() == None)

    unittest.main()
