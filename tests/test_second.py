import unittest
from server import some_random_function

class TestCase:
    def __init__(self, case, expected_match):
        self.case = case
        self.expected_match = expected_match

class MyTestCase(unittest.TestCase):
    def do_some_testing(self):
        # check if these things match
        test_cases = [
            TestCase("something", "something"),
            TestCase("something else", "something else"),
        ]
        for test_case in test_cases:
            self.assertEqual(test_case.case, some_random_function(test_case.case))





if __name__ == '__main__':
    unittest.main()