from unittest import TestCase
import json
import pprint

# run with python -m unitttest file_name.py for just this file
# run with python -m unittest discover to discover all files prefixed with test and run them

whatever_data = [
    {
        'This' : 'That'
    },
    {
        'This' : 'That'
    },
    {
        'This' : 'That'
    }
]

class MyTest(TestCase):
    def some_test(self):
        # run some logic stuff
        self.assertEqual(len(whatever_data), 3)
